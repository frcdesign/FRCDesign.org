from __future__ import annotations

import manim as mn
from typing import Callable

from library.style import color
from library.math import tangent, vector
from library.design import sketch
from library.utils.type_utils import not_none


class PlateCircle(sketch.Circle):
    def __init__(self, inner_circle: mn.Circle, outer_circle: mn.Circle) -> None:
        self.inside = inner_circle
        self.outside = outer_circle
        super().__init__(self.outside)

        def follow(mobject: mn.Mobject) -> None:
            mobject.move_to(self.get_center())

        self.inside.add_updater(follow, call_updater=True)

    def get_inner_radius(self) -> float:
        return self.inside.radius

    def get_outer_radius(self) -> float:
        return self.outside.radius

    def get_group(self) -> mn.VGroup:
        return mn.VGroup(self.inside, super().get_group())

    def click_target(self) -> mn.VMobject:
        return self.outside


def plate_circle_tangent_points(
    start: PlateCircle, end: PlateCircle
) -> tuple[vector.Point2d, vector.Point2d]:
    return tangent.circle_to_circle_tangent(
        start.get_center(),
        start.get_outer_radius(),
        end.get_center(),
        end.get_outer_radius(),
    )


def plate_circle_tangent_line(start: PlateCircle, end: PlateCircle) -> sketch.Line:
    return sketch.make_line(*plate_circle_tangent_points(start, end))


PlateCircleGenerator = Callable[[vector.Point2d], PlateCircle]


class PlateCircleFactory:
    def __init__(self) -> None:
        self._inner_color: color.Color = color.FOREGROUND
        self._outer_color: color.Color = color.FOREGROUND

    def set_inner_color(self, color: color.Color) -> PlateCircleFactory:
        self._inner_color = color
        return self

    def set_outer_color(self, color: color.Color) -> PlateCircleFactory:
        self._outer_color = color
        return self

    def make_generator(self, radius: float, offset: float) -> PlateCircleGenerator:
        """
        Returns a generator function which may be used to create points of the given size.
        The generator function takes a location as an argument.
        """

        def generator(point: vector.Point2d) -> PlateCircle:
            return PlateCircle(
                mn.Circle(radius, color=self._inner_color, arc_center=point),
                mn.Circle(radius + offset, color=self._outer_color, arc_center=point),
            )

        return generator

    def make(
        self, radius: float, offset: float, location: vector.Point2d
    ) -> PlateCircle:
        # get a generator and immediately pass it location
        return self.make_generator(radius, offset)(location)


class PlateGroup(mn.VGroup):
    def __init__(
        self,
        entities: list[PlateCircle],
        boundary_order: list[int],
        # boundary_color: color.Color = color.FOREGROUND,
    ) -> None:
        self._entities: list[PlateCircle] = entities
        self._boundary: list[PlateCircle] = [self._entities[i] for i in boundary_order]
        self._boundary_lines: list[sketch.Line] = self._make_boundary_lines()
        super().__init__(*[*self._entities, *self._boundary_lines])

    def _make_boundary_lines(self) -> list[sketch.Line]:
        return [
            plate_circle_tangent_line(self._boundary[i - 1], curr)
            for i, curr in enumerate(self._boundary)
        ]

    def draw_inner_circles(self) -> mn.Animation:
        return not_none(
            mn.Succession(
                *[mn.GrowFromCenter(x.inside) for x in self._entities], lag_ratio=0.75
            )
        )

    def draw_outer_circles(self) -> mn.Animation:
        return not_none(
            mn.Succession(
                *[mn.GrowFromCenter(x.outside) for x in self._entities], lag_ratio=0.75
            )
        )

    def draw_boundary(self) -> mn.Animation:
        return not_none(
            mn.Succession(
                *[mn.Create(line) for line in self._boundary_lines], lag_ratio=1
            )
        )
