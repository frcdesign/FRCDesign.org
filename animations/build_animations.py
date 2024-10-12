"""
A build script which can be used to compile animations and build the website.

Fuzzy matching is used to enable quickly specifying targets in the animations sub-folder.
"""

import inspect
import os
import subprocess
import argparse
import time
import pathlib
import importlib
import re
import asyncio

from thefuzz import process, fuzz
import manim as mn

# The path to search for animations
source_path = pathlib.Path("animations/animations")

quality_folder_lookup = {"l": "480p15", "m": "720p30", "h": "1080p60"}

exclude_folders = ["__pycache__", "media", "_style"]

# A regex used to split animation names
split_regex = "A-Z_/\\\\"


def get_all_file_paths(base: pathlib.Path) -> list[pathlib.Path]:
    """Searches source_path for all potential files. Returns a mapping of file names to their paths."""
    return [
        file_path for file_path in base.glob("**/*.py") if file_path.name != "conf.py"
    ]


def get_all_paths() -> list[pathlib.Path]:
    """Searches source_path for all possible paths, including sub-paths, and returns them.

    This function is used to collect paths for matching with the -p option.
    The paths include paths to all files.
    """
    return [
        pathlib.Path(*path.parts[1:])
        for path in source_path.glob("**")
        if path.name not in exclude_folders
    ]


def get_all_scenes(file_paths: list[pathlib.Path]) -> dict[str, pathlib.Path]:
    """Searches source_path for all possible scenes.

    Returns a mapping of scenes to their files.
    Duplicate scenes and files are not explicitly handled.
    """
    return dict(
        [
            (scene_name, file_path)
            for file_path in file_paths
            for scene_name in get_scene_names(file_path)
        ]
    )


def get_scene_names(file_path: pathlib.Path) -> list[str]:
    """Extracts a list of scene names from the file specified by file_path."""
    module_path = str(file_path).replace("/", ".").removesuffix(".py")
    module = importlib.import_module(module_path)
    return [
        name
        for name, cls in inspect.getmembers(module)
        if inspect.isclass(cls)
        and issubclass(cls, mn.Scene)
        and cls.__module__ == module_path
    ]


def move_output(quality: str, file_path: pathlib.Path, scene_name: str) -> None:
    """Moves produced files from media to the appropriate location in website."""
    quality_folder = quality_folder_lookup[quality]

    path, sub_folder = os.path.split(file_path)

    # -p suppresses errors
    # subprocess.run(f"mkdir -p {path}/media", shell=True)
    subprocess.run(f"mkdir -p videos", shell=True)

    # for scene in scenes:
    # {path}/media/.
    move_command = "mv media/videos/{sub_folder}/{quality_folder}/{scene_name}.mp4 videos/.".format(
        sub_folder=sub_folder.removesuffix(".py"),
        scene_name=scene_name,
        quality_folder=quality_folder,
        path=path,
    )
    subprocess.run(move_command, shell=True)


def get_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Builds animations.",
    )
    parser.add_argument(
        "--production",
        action="store_true",
        help="whether to build production versions of animations",
    )

    parser.add_argument(
        "-m",
        "--make",
        action="store_true",
        help="whether to make the website after building",
    )

    description = """
    Inputs to the builder. All inputs are parsed using a fuzzy matcher which enables (often aggressive) abbreviations.
    The fuzzer works by comparing tokens in the input with target tokens. 
    Token splits are determined using capital letters, slashes, backslashes, and underscores.
    So, "CoLi" or "coLi" will match "CoincidentLine" better than "coli" or "COLI".
    """

    group = parser.add_argument_group("inputs", description)

    group.add_argument(
        "-f",
        "--file",
        nargs="*",
        default=None,
        help="python files to build",
    )
    group.add_argument(
        "-p",
        "--path",
        nargs="*",
        default=None,
        help='paths relative to "/{}" which are recursively searched for files'.format(
            source_path
        ),
    )
    group.add_argument(
        "-s",
        "--scene",
        nargs="*",
        help="a list of scenes to render",
    )
    return parser


def fuzzy_search(targets: list[str], values: list[str]) -> list[str]:
    parsed_targets = dict([(target, split_tokens(target)) for target in targets])

    matches = []
    for value in values:
        parsed_value = split_tokens(value)
        _, score, target_name = process.extractOne(  # type: ignore
            parsed_value, parsed_targets, scorer=fuzz.token_sort_ratio  # type: ignore
        )

        if score < 95:
            print("Found {} for input {} (score: {})".format(target_name, value, score))
        # print("Inputs:", parsed_targets)
        # print("Query:", parsed_value)
        matches.append(target_name)
    return matches


def split_tokens(input: str) -> str:
    parsed = re.search("[^{}]*".format(split_regex), input)
    matches: list[str] = []
    if parsed is not None:
        matches.append(parsed.group(0))

    end = re.findall("[{}][^{}]*".format(split_regex, split_regex), input)
    matches.extend(end)
    return " ".join(matches)


async def render_scene(quality: str, scene_name: str, file_path: pathlib.Path):
    manim_command = f"manim render -v ERROR -q{quality} {file_path} {scene_name}"

    print(f"Rendering {file_path} - {scene_name}")
    process = await asyncio.create_subprocess_shell(manim_command)
    await process.wait()
    move_output(quality, file_path, scene_name)


async def main():
    args = get_arg_parser().parse_args()

    quality = "m" if args.production else "l"

    target_paths = []
    if args.path is not None:
        all_paths = get_all_paths()
        all_path_strs = [str(path) for path in all_paths]
        results = fuzzy_search(all_path_strs, args.path)
        file_path_lists = [
            get_all_file_paths(source_path / pathlib.Path(path)) for path in results
        ]
        target_paths = [item for sublist in file_path_lists for item in sublist]

    else:
        target_paths = get_all_file_paths(source_path)

    if args.file is not None:
        # we use a dict so we can split names into sequences
        target_names = [path.name for path in target_paths]
        results = fuzzy_search(target_names, args.file)
        target_paths = [path for path in target_paths if path.name in results]

    scenes = get_all_scenes(target_paths)
    if args.scene is not None:
        results = fuzzy_search(list(scenes.keys()), args.scene)
        scenes = dict([(k, v) for k, v in scenes.items() if k in results])

    start = time.time()
    async with asyncio.TaskGroup() as tg:
        for scene_name, file_path in scenes.items():
            tg.create_task(render_scene(quality, scene_name, file_path))
    end = time.time()
    duration = round(end - start, 2)
    print(f"Built {len(scenes)} scenes in {duration} seconds")

    if args.make:
        subprocess.run("mkdocs build", shell=True)


if __name__ == "__main__":
    asyncio.run(main())
