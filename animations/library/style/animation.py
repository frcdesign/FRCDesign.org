"""
Style elements intrinsically linked with animation, such as timing.
"""

from typing import override
import manim as mn
from library.utils.type_utils import ALMOST_ZERO
from library.style import color
from library.math import vector

END_DELAY = 2.5


class ShrinkToPoint(mn.Transform):
    """Removes a mobject by shrinking it to point."""

    def __init__(
        self,
        mobject: mn.Mobject,
        point: vector.Point2d,
        point_color: color.Color | None = None,
        **kwargs,
    ) -> None:
        self.point = point
        self.point_color = point_color
        super().__init__(mobject, remover=True, reverse_rate_function=True, **kwargs)

    def create_target(self) -> mn.Mobject:
        return self.mobject

    def create_starting_mobject(self) -> mn.Mobject:
        start = super().create_starting_mobject()
        start.scale(0).move_to(self.point)
        if self.point_color:
            start.set_color(self.point_color)  # type: ignore
        return start


class ShrinkToCenter(ShrinkToPoint):
    """Remove a mobject by shrinking it to its center."""

    def __init__(
        self, mobject: mn.Mobject, point_color: color.Color | None = None, **kwargs
    ) -> None:
        super().__init__(
            mobject, mobject.get_center(), point_color=point_color, **kwargs
        )


class Add(mn.Animation):
    def __init__(self, *mobjects: mn.VMobject, almost_zero: bool = False):
        super().__init__(
            mn.VGroup(*mobjects),
            introducer=True,
            run_time=(ALMOST_ZERO if almost_zero else 0),
        )

    # Override begin to allow run_time of 0
    @override
    def begin(self) -> None:
        self.starting_mobject = self.create_starting_mobject()
        if self.suspend_mobject_updating:
            self.mobject.suspend_updating()
        self.interpolate(0)


class Remove(mn.Animation):
    def __init__(self, *mobjects: mn.VMobject, almost_zero: bool = False):
        # Has to also be an introducer to allow updaters to run for some reason
        super().__init__(
            mn.VGroup(*mobjects),
            introducer=True,
            remover=True,
            run_time=(ALMOST_ZERO if almost_zero else 0),
        )

    @override
    def begin(self) -> None:
        self.starting_mobject = self.create_starting_mobject()
        if self.suspend_mobject_updating:
            self.mobject.suspend_updating()
        self.interpolate(0)
