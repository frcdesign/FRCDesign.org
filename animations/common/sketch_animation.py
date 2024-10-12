from typing import cast
import manim as mn
from animations.common import sketch
from animations.style import color


# doesn't work as a class member...
Z_INDEX = 500


class Click(mn.Transform):
    """Defines an animation which represents an object getting clicked."""

    def __init__(self, mobject: sketch.Base):
        base = mobject.click_target()
        target = base.copy().set_stroke(width=4 * 3.5).set_color(color.Palette.YELLOW)  # type: ignore

        # set z_index to make highlight go over the top (a bit suss)
        global Z_INDEX
        base.set_z_index(Z_INDEX)
        Z_INDEX += 1

        super().__init__(
            base, target_mobject=target, rate_func=mn.there_and_back, run_time=0.75
        )


def make(animation: mn.Animation, *mobjects: sketch.Base) -> mn.Succession:
    """Defines a step in an animation.

    Each mobject is clicked in sequence, followed by the final animation playing.
    """
    return cast(
        mn.Succession,
        mn.Succession(*[Click(mobject) for mobject in mobjects], animation),
    )
