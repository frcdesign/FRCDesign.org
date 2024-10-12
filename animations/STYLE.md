# Style

This document describes the style guide for the website and animations.

# Animations

## Timing

Avoid running animations with non-standard units of time. Prefer using one of the following values:
`0, 0.25, 0.5, 0.75, 1, 1.5, 2, 2.5, 3, 4, 5...`
When setting the pace of an animation, consider that animations may play in a format which is not easily
pausable, and that many users prefer a slower format.

Animations should always finish with a delay equal to `style.animation.END_DELAY`.

## Colors

Use the `Color` type and colors defined in `style`. Do not use colors from manim directly.

## Building Animations

Animations used on the live website should be built as `gif`s with medium (`-qm`) quality. The output file
name (`-o [FILENAME]`) should be lowercase with underscores for spaces.

```
%%manim -v CRITICAL --format gif --disable_caching -qm -o boundary_constraints BoundaryConstraintScene
```

# Code

## Writing Animations

Animation helpers and members should be marked with `_`.
`setup` should be used to set constant data for scenes.
Large animations may choose to abbreviate `self` as `s`.
Scenes should not be passed as arguments to classes without good reason.

## Classes

### Naming

Class members should generally be marked private by prepending an underscore, e.g. `_my_value`.
Internal class methods should also be marked private by prepending an underscore, e.g. `_internal_func`.

Setters should be prepended with `set`. Note setters should be made chainable by having them
return an instace of themselves.

Getters may be prepended with `get`, but this is optional. Prefer writing a `getter` over making a
value `public`.

### Chaining

Setters, as well as other methods with no default return value, should generally enable chaining
by returning an instance of themselves (Typed using `Self`).

### Factories

Classes with factory methods should include the methods as static members and name them `make`.

Do not require calling setter methods between initialization of a class and use of a class method.
For non-trivial classes, prefer to use direct injection and write factories instead of writing
complex constructors.

## Imports

Avoid polluting namespaces by importing with `*`.
Manim may be imported using `from Manim import *`.
Import user types using `from rc_lib import math_types as T`. Import other custom types directly.

## Types

Classes should be typed using Python type hints. The following rules apply:

- Type the return type of `__init__` methods with `None`.
- Use defined types from `math_types` and elsewhere as appropriate. Avoid using `np.ndarray` directly.
- User defined types may be imported aliased as `T`.
- Union types should be defined using Python 10 `|` syntax, e.g. `str | None` instead of `Optional[str]`.
- Note `Optional` is used for kwargs which are intended to allow explicitly passing the value `None`. This should not be confused
  with not passing the type at all.
- Use `Self` when a method returns an instance of it's own class.
- Type returns using the base class. For example, return an `Animation`, not a `Succession`, and a `VMObject`, not a `VGroup`.

## Spelling

Spellings not recognized by the spellchecker should either corrected or added to the `.vscode` workspace settings using the quick fix menu.

## Manim Bugs

### Resolved Bugs

`angle_between_vectors`'s return type is incorrectly typed as `np.ndarray`, not `float`.

`mn.Arc`'s `start_angle` is typed as `int`, not `float` (since the type of `0` defaults to `int`)
"animation" is spelled "animnation" in add_animation_override docs

### Trivial Fixes

`mobject.add_updater`'s call_updater argument throws when the updater does not take dt as an argument (as updater call logic for handling dt is missing)
Update: This will be resolved in the next release of manim.

### Bigger Issues

`GrowFromCenter` should probably expose introducer (like Create and Uncreate do)

AnimationBuilders from .animate are not valid animations.

`get_x`, `get_y`, and `get_z` are the only functions to use/return `np.float64`

`mn.Color` seems to be incompatible with raw `str`; this problem is worsened by `mn.Color` not being exposed.
`GrowFromCenter` and `GrowFromPoint`'s colors are typed as `str`, not `Color` and are missing `| None`.
Update: These issues are being addressed by the upcoming color refactor.

`Sequence[float]`, `np.ndarray`, and sometimes `Sequence[float] | np.ndarray` are used somewhat interchangably.
Since `np.ndarray` is not compatible with `Sequence[float]`, there are annoying behaviors like
the types of `line.put_start_and_end_on` not being compatible with, e.g. `line.get_start`.

`remover` animations break updaters, even when used after normal animations in a `Succession`. However, this behavior goes
away if `introducer` is set to `True` on the remover animation.

### Features

I would like `Add` and `Delete` type animations which add and delete objects from a scene and have a run-time of `0`.
This would be useful for, e.g., creating objects in class methods which do not have access to `Scene` directly.
