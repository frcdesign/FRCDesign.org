from typing import TypeAlias

import manim as mn
import enum
import math
import numpy as np

Color: TypeAlias = str


class Palette(Color, enum.Enum):
    """
    General-purpose palette.

    Prefer using one of the color generator methods when choice of color is
    arbitrary.
    """

    RED = mn.RED
    GREEN = mn.GREEN
    BLUE = mn.BLUE
    YELLOW = mn.YELLOW
    WHITE = mn.WHITE
    BLACK = mn.BLACK


FOREGROUND: Color = Palette.WHITE


class CategoricalPalette(Color, enum.Enum):
    """
    Based on Tol Vibrant.

    Instead of using this class directly, prefer using color_categories
    to generate colors.
    """

    BLUE = "#0077BB"
    CYAN = "#33BBEE"
    TEAL = "#009988"
    RED = "#CC3311"
    ORANGE = "#EE7733"
    MAGENTA = "#EE3377"


def color_categories(n_categories: int):
    """
    Returns a palette of colors meeting the required amount of categories.

    Do not use for more than 6 categories: overuse of color becomes overwhelming
    and confusing, and it is hard to find a colorblind-friendly palette with
    many colors. Consider reducing your scenes reliance on color.
    """
    order = [
        CategoricalPalette.BLUE,
        CategoricalPalette.ORANGE,
        CategoricalPalette.MAGENTA,
        CategoricalPalette.CYAN,
        CategoricalPalette.RED,
        CategoricalPalette.TEAL,
    ]

    assert n_categories <= len(order)

    return order[:n_categories]


def _unit_interpolate_colors(colors: list[Color]):
    """
    Returns a function that, when given an float index 0 <= i <= 1, returns
    the interpolated color from the list.
    """

    def get_color(i):
        index = i * (len(colors) - 1)

        # find two nearest colors and interpolate
        lower = math.floor(index)
        upper = math.ceil(index)
        interp = index - lower

        return mn.color.interpolate_color(colors[lower], colors[upper], interp)

    return get_color


def _rebind_scale(f, old_range: tuple[float, float], new_range: tuple[float, float]):
    """
    Rebinds a single-scalar input function so that it operates identically
    on a new interval.
    """
    new_span = new_range[1] - new_range[0]
    old_span = old_range[1] - old_range[0]

    assert abs(new_span) > np.finfo(float).eps, "Range must have non-zero width"

    def rebind(x: float):
        # change to interpolation from endpoint 1
        x = (x - new_range[0]) / new_span

        # convert back to old range
        x = (old_span * x) + old_range[0]

        return f(x)

    return rebind


def sequential_colors(range=(0, 1)):
    """
    Returns a function that can be used to generate colors indicating scale.

    Args:
        range = (start, stop): The range of inputs to bind the colors to.
            `start` corresponds to the value with lowest-scale color, and `stop`
            corresponds to the highest-scale.
            Moving from start towards top is seen as increasing the scale,
            so if start < stop decreasing the value can increase the scale
            of its color.
    """

    # Viridis color scale
    colors: list[Color] = [
        "#440154",
        "#414487",
        "#2A788E",
        "#22A884",
        "#FDE725",
    ]  # low  # high

    unit_sequential = _unit_interpolate_colors(colors)
    return _rebind_scale(unit_sequential, (0, 1), range)


def divergent_colors(range=(-1, 1)):
    """
    Returns a function that can be used to generate colors indicating scale.

    Args:
        range = (start, stop): The range of inputs to bind the colors to.
            `start` corresponds to the value with lowest-scale color, and `stop`
            corresponds to the highest-scale.
            Moving from start towards top is seen as increasing the scale,
            so if start < stop decreasing the value can increase the scale
            of its color.
    """

    # Blue-Orange scale
    colors: list[Color] = [
        CategoricalPalette.BLUE,  # negative
        "#EAECCC",  # zero
        CategoricalPalette.RED,  # positive
    ]

    unit_divergent = _unit_interpolate_colors(colors)
    return _rebind_scale(unit_divergent, (0, 1), range)
