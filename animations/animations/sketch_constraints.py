"""Animations showcasing various Onshape sketch constraints."""

import math

import manim as mn

from library.math import vector
from library.design import sketch, sketch_scene, constraint, sketch_animation
from library.utils.type_utils import not_none


def coincident_common_mobjects() -> tuple[sketch.Circle, sketch.Line, sketch.Line]:
    """Returns mobjects common to coincident point scenes."""
    return (
        sketch.make_circle(vector.point_2d(-4.5, 0), 1.5),
        sketch.make_line(vector.point_2d(5.25, 4 / 2), vector.point_2d(5.25, -4 / 2)),
        sketch.make_line(vector.point_2d(-1.75, 0.75), vector.point_2d(4.25, -1)),
    )


class CoincidentPointsScene(sketch_scene.Scene):
    def construct(self) -> None:
        circle, line, move_line = coincident_common_mobjects()
        self.introduce(circle, line, move_line)
        self.run_group(constraint.Coincident(move_line.start, circle.middle))
        self.run_group(constraint.Coincident(move_line.end, line.end))


class CoincidentPointLineScene(sketch_scene.Scene):
    def construct(self) -> None:
        circle, line, move_line = coincident_common_mobjects()
        self.introduce(circle, line, move_line)
        self.run_group(constraint.Coincident(move_line.start, circle))
        self.run_group(constraint.Coincident(move_line.end, line))


class CoincidentLineScene(sketch_scene.Scene):
    def construct(self) -> None:
        start_point = vector.point_2d(-5.75, 2.5)
        middle_point = vector.point_2d(-1.15, 0.5)  # closest to the middle
        fixed_line = sketch.make_line(start_point, middle_point)

        slope = fixed_line.get_direction()
        angle = math.radians(38)
        start_line = sketch.make_line(
            middle_point + mn.rotate_vector(slope * 2, angle),
            middle_point + mn.rotate_vector(slope * 7.5, angle),
        )

        self.introduce(fixed_line, start_line)

        animation = mn.Rotate(start_line, -angle, about_point=fixed_line.get_end())
        self.run_group(sketch_animation.make(animation, start_line, fixed_line))


def align_common_line() -> sketch.Line:
    return sketch.make_line(vector.point_2d(-2.3, -2.3), vector.point_2d(2.3, 2.3))


class VerticalLineScene(sketch_scene.Scene):
    def construct(self) -> None:
        start_line = align_common_line()
        self.introduce(start_line)
        self.run_group(constraint.Vertical(line=start_line))


class HorizontalLineScene(sketch_scene.Scene):
    def construct(self) -> None:
        start_line = align_common_line()
        self.introduce(start_line)
        self.run_group(constraint.Horizontal(line=start_line))


class VerticalPointsScene(sketch_scene.Scene):
    def construct(self) -> None:
        circle = sketch.make_circle(vector.point_2d(-4, 1.5), 1.5)
        line = sketch.make_line(vector.point_2d(0, 2.5), vector.point_2d(5.5, 1.5))
        move_line = sketch.make_line(
            vector.point_2d(-5.5, -2.5), vector.point_2d(3.5, -1.5)
        )

        self.introduce(circle, line, move_line)
        self.run_group(constraint.Vertical(points=(move_line.start, circle.middle)))
        self.run_group(constraint.Vertical(points=(move_line.end, line.end)))


class HorizontalPointsScene(sketch_scene.Scene):
    def construct(self) -> None:
        circle = sketch.make_circle(vector.point_2d(-3.5, 1.5), 1.5)
        line = sketch.make_line(vector.point_2d(-5, -0.75), vector.point_2d(-1, -2.5))
        move_line = sketch.make_line(vector.point_2d(2, -1.5), vector.point_2d(4.5, 3))

        self.introduce(circle, line, move_line)
        self.run_group(constraint.Horizontal(points=(move_line.start, line.end)))
        self.run_group(constraint.Horizontal(points=(move_line.end, circle.middle)))


class ParallelScene(sketch_scene.Scene):
    def construct(self) -> None:
        line = sketch.make_line(vector.point_2d(-6, -3), vector.point_2d(6, 0.5))
        direction = line.get_direction()

        end_point = vector.point_2d(5, 3)
        start_point = end_point - direction * 10.5
        angle = math.radians(16.26)
        start_line = sketch.make_line(start_point, end_point).rotate(
            -angle, about_point=line.get_midpoint()
        )

        animation = not_none(
            mn.Rotate(start_line, angle, about_point=line.get_midpoint())
        )
        self.introduce(line, start_line)
        self.run_group(sketch_animation.make(animation, start_line, line))


class PerpendicularScene(sketch_scene.Scene):
    def construct(self) -> None:
        line = sketch.make_line(vector.point_2d(-5, -2.75), vector.point_2d(5.5, 0.5))
        direction = line.get_direction()
        rotation_point = line.get_start() + direction * 2
        perpendicular_direction = vector.direction_2d(-direction[1], direction[0])

        angle = math.radians(45)
        start_line = sketch.make_line(
            rotation_point + perpendicular_direction * 1,
            rotation_point + perpendicular_direction * 5.25,
        ).rotate(-angle, about_point=rotation_point)

        self.introduce(start_line, line)
        self.run_group(
            sketch_animation.Click(start_line),
            sketch_animation.Click(line),
            # rotate to end position
            start_line.animate.rotate(angle, about_point=rotation_point),
        )


class EqualLineScene(sketch_scene.Scene):
    def construct(self) -> None:
        base = sketch.make_line(vector.point_2d(-5.5, -1.5), vector.point_2d(-1.25, 2))
        first = sketch.make_line(vector.point_2d(-5, -3), vector.point_2d(5, -1))
        second = sketch.make_line(vector.point_2d(-0.5, 2.75), vector.point_2d(6, 0.5))

        self.introduce(base, first, second)
        self.run_group(constraint.Equal(base, first))
        self.run_group(constraint.Equal(base, second))


class EqualCircleScene(sketch_scene.Scene):
    def construct(self) -> None:
        base = sketch.make_circle(vector.point_2d(0, -1.5), 1.5)
        circle = sketch.make_circle(vector.point_2d(-3.5, 1), 2)
        arc = sketch.make_arc(
            vector.point_2d(3.5, 1), 2, math.radians(90), math.radians(-225)
        )

        self.introduce(base, arc, circle)
        self.run_group(constraint.Equal(base, circle))
        self.run_group(constraint.Equal(base, arc))


class MidpointLineScene(sketch_scene.Scene):
    def construct(self) -> None:
        top = sketch.make_line(vector.point_2d(-6, 3), vector.point_2d(6, 1.25))
        bottom = sketch.make_line(vector.point_2d(-6, -3), vector.point_2d(6, -1.25))
        middle = sketch.make_line(vector.point_2d(-1, 1.5), vector.point_2d(1, -1.5))

        self.introduce(top, bottom, middle)
        self.run_group(constraint.Midpoint(middle.start, line=top))
        self.run_group(constraint.Midpoint(middle.end, line=bottom))


class MidpointPointScene(sketch_scene.Scene):
    def construct(self) -> None:
        line = sketch.make_line(vector.point_2d(-6, 5 / 2), vector.point_2d(-6, -5 / 2))
        circle = sketch.make_circle(vector.point_2d(4.5, 0), 1.5)
        first_line = sketch.make_line(vector.point_2d(-1.5, 2), vector.point_2d(0, -2))
        second_line = sketch.make_line(
            vector.point_2d(-5.25, -0.5), vector.point_2d(-1.5, 0.5)
        )

        self.introduce(line, circle, first_line)
        self.run_group(
            constraint.Midpoint(first_line.start, points=(line.start, circle.middle))
        )
        self.run_group(
            constraint.Midpoint(first_line.end, points=(line.end, circle.middle))
        )

        self.introduce(second_line)
        self.run_group(
            constraint.Midpoint(second_line.start, points=(line.start, line.end))
        )
        self.run_group(
            constraint.Midpoint(
                second_line.end, points=(first_line.start, first_line.end)
            )
        )


class TangentLineScene(sketch_scene.Scene):
    def construct(self) -> None:
        circle = sketch.make_circle(mn.ORIGIN, 1.5)
        left = sketch.make_line(vector.point_2d(-6, 0), vector.point_2d(0, 2.75))
        right = sketch.make_line(vector.point_2d(2, -2.5), vector.point_2d(6, -2))

        self.introduce(circle, left, right)
        self.run_group(constraint.Tangent(left, circle))
        self.run_group(constraint.Tangent(right, circle))


class TangentCircleScene(sketch_scene.Scene):
    def construct(self) -> None:
        circle = sketch.make_circle(mn.ORIGIN, 1.5)
        left = sketch.make_circle(vector.point_2d(-4, 1), 1.5)
        right = sketch.make_arc(
            vector.point_2d(6, -1.125), 3.5, math.radians(105), math.radians(75)
        )

        self.introduce(circle, left, right)
        self.run_group(constraint.Tangent(left, circle))
        self.run_group(constraint.Tangent(right, circle))


def concentric_common() -> tuple[sketch.Circle, sketch.Circle, sketch.Arc]:
    return (
        sketch.make_circle(mn.ORIGIN, 1.5),
        sketch.make_circle(vector.point_2d(-4, 0), 2),
        sketch.make_arc(vector.point_2d(3, 0), 3, math.radians(70), math.radians(-140)),
    )


class ConcentricEdgeScene(sketch_scene.Scene):
    def construct(self) -> None:
        circle, left, right = concentric_common()
        self.introduce(circle, left, right)
        # move to origin using shift
        self.run_group(constraint.Concentric(left, circle))
        # click larger circle
        self.run_group(constraint.Concentric(right, left))


class ConcentricPointScene(sketch_scene.Scene):
    def construct(self) -> None:
        circle, left, right = concentric_common()
        self.introduce(circle, left, right)
        self.run_group(constraint.Concentric(left.middle, circle))
        self.run_group(constraint.Concentric(right.middle, circle))
