import manim as mn
from typing import Callable, Self

from animations.utils.type_utils import ALMOST_ZERO
from animations.style import animation
from animations.style import color
from animations.geometry import tangent, vector
from animations.common import sketch


class PlateCircle(sketch.Circle):
    """Adds a second, outer circle around the inner sketch circle."""

    def __init__(self, inner_circle: mn.Circle, outer_circle: mn.Circle) -> None:
        self.inside = inner_circle
        self.outside = outer_circle
        super().__init__(self.outside)

        def follow(mobject: mn.Mobject) -> None:
            mobject.move_to(self.get_center())

        self.inside.add_updater(follow)

    def get_inner_radius(self) -> float:
        return self.inside.get_radius()

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

    def set_inner_color(self, color: color.Color) -> Self:
        self._inner_color = color
        return self

    def set_outer_color(self, color: color.Color) -> Self:
        self._outer_color = color
        return self

    def make_generator(self, radius: float, offset: float) -> PlateCircleGenerator:
        """
        Returns a generator function which may be used to create points of the given size.
        The generator function takes a location as an argument and returns PlateCircles.
        """

        def generator(point: vector.Point2d) -> PlateCircle:
            return PlateCircle(
                mn.Circle(radius=radius, color=self._inner_color, arc_center=point),
                mn.Circle(
                    radius=radius + offset, color=self._outer_color, arc_center=point
                ),
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
        boundary_indices: list[int],
        # boundary_color: color.Color = color.FOREGROUND,
    ) -> None:
        """
        Params:
            entities: A list of PlateCircles to draw.
            boundary_order: A list of indicies into `entities` specifying the boundary of the plate.
        """
        self._entities: list[PlateCircle] = entities
        self._boundary_indices = boundary_indices
        self._boundary: list[PlateCircle] = [
            self._entities[i] for i in boundary_indices
        ]
        self._boundary_lines: list[sketch.Line] = self._make_boundary_lines()
        super().__init__(*[*self._entities, *self._boundary_lines])

    def _make_boundary_lines(self) -> list[sketch.Line]:
        return [
            # line[i] connects curr[i-1] and curr[i]
            plate_circle_tangent_line(self._boundary[i - 1], curr)
            for i, curr in enumerate(self._boundary)
        ]

    def draw_inner_circles(self) -> mn.Animation:
        return mn.Succession(
            *[mn.GrowFromCenter(x.inside) for x in self._entities], lag_ratio=0.75
        )

    def draw_outer_circles(self) -> mn.Animation:
        return mn.Succession(
            *[mn.GrowFromCenter(x.outside) for x in self._entities], lag_ratio=0.75
        )

    def draw_boundary(self) -> mn.Animation:
        return mn.Succession(
            *[mn.Create(line) for line in self._boundary_lines], lag_ratio=1
        )

    def _trim_boundary_circle(self, boundary_i: int) -> mn.Animation:
        boundary = self._boundary[boundary_i]
        # line[i] connects boundary[i-1] to boundary[i]
        # so boundary[i] needs line[i] and line[i + 1]
        start_point = self._boundary_lines[boundary_i].get_end()
        end_point = self._boundary_lines[
            (boundary_i + 1) % len(self._boundary_lines)
        ].get_start()
        boundary_arc = mn.ArcBetweenPoints(
            # Draw clockwise from end to start
            end_point,
            start_point,
            radius=boundary.get_outer_radius(),
            color=boundary.outside.color,
        )
        start_angle = mn.angle_of_vector(start_point - boundary.get_center())
        angle = (2 * mn.PI) - vector.angle_between_points(
            start_point, end_point, boundary.get_center()
        )
        inside_arc = mn.Arc(
            start_angle=start_angle,
            angle=angle,
            radius=boundary.get_outer_radius(),
            arc_center=boundary.get_center(),
            color=boundary.circle.color,
        )
        return mn.Succession(
            # animation.Remove doesn't work here for some dumb reason
            mn.Uncreate(boundary.outside, run_time=ALMOST_ZERO),
            animation.Add(boundary_arc, inside_arc),
            mn.Uncreate(inside_arc),
            run_time=0.75,
        )

    def trim_boundary(self) -> mn.Animation:
        animations = []
        for i, entity in enumerate(self._entities):
            if i in self._boundary_indices:
                # Get index into self._boundary
                boundary_i = self._boundary_indices.index(i)
                animations.append(self._trim_boundary_circle(boundary_i))
            else:
                animations.append(mn.Uncreate(entity.outside, run_time=0.75))

        return mn.Succession(*animations, lag_ratio=0.75)
