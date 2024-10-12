# Animations

This folder contains Python code for specifying and creating animations using Manim Community.
Specifying animations in Python allows for precise programmatic control over content, which is great for showcasing simple behaviors.

# Style

## Timing

Avoid running animations with non-standard units of time. Prefer using one of the following values:
`0, 0.25, 0.5, 0.75, 1, 1.5, 2, 2.5, 3, 4, 5...`
When setting the pace of an animation, consider that animations may play in a format which is not easily
pausable, and that many users prefer a slower format.

Animations should always finish with a delay equal to `style.animation.END_DELAY`.

## Colors

Use the `Color` type and colors defined in `style`. Do not use colors from manim directly.

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