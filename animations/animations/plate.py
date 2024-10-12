"""Animations which model basic plates."""

import manim as mn
from animations.style import color, animation
from animations.geometry import vector
from animations.utils import title_sequence
from animations.common import plate, sketch, constraint

inner_color: color.Color = color.Palette.GREEN
boundary_color: color.Color = color.Palette.BLUE

plate_factory: plate.PlateCircleFactory = plate.PlateCircleFactory()
plate_factory.set_inner_color(inner_color).set_outer_color(boundary_color)

title: title_sequence.TitleSequence = title_sequence.TitleSequence(
    default_color=boundary_color
)


class IntakePlateScene(mn.Scene):
    def setup(self):
        small_base: plate.PlateCircleGenerator = plate_factory.make_generator(0.15, 0.2)
        medium_base: plate.PlateCircleGenerator = plate_factory.make_generator(0.4, 0.2)

        front_hole = vector.point_2d(-4, -3)
        middle_hole = vector.point_2d(-1.5, 0.25)
        back_hole = vector.point_2d(2.5, 1.5)

        circles: list[plate.PlateCircle] = [
            medium_base(front_hole),
            medium_base(middle_hole),
            medium_base(back_hole),
            small_base(back_hole + vector.vector_2d(0.8, 0.75)),
            small_base(back_hole + vector.vector_2d(1, -0.2)),
            small_base((middle_hole + back_hole) / 2),
            small_base((front_hole + middle_hole) / 2),
        ]
        boundary_order: list[int] = [1, 3, 4, 0]
        self._plate_group: plate.PlateGroup = plate.PlateGroup(circles, boundary_order)
        title.reset()

    def construct(self):
        self.play(title.next("Draw plate holes", color=inner_color))
        self.play(self._plate_group.draw_inner_circles())

        self.play(title.next("Add larger circles"))
        self.play(self._plate_group.draw_outer_circles())

        self.play(title.next("Connect boundary"))
        self.play(self._plate_group.draw_boundary())

        self.play(title.next("Trim circles"))
        self.play(self._plate_group.trim_boundary())

        self.wait(animation.END_DELAY)


class BoundaryRedrawScene(mn.Scene):
    def setup(self):
        generator: plate.PlateCircleGenerator = plate_factory.make_generator(1.75, 0.75)
        self._left: plate.PlateCircle = generator(vector.point_2d(-6, -2))
        self._right: plate.PlateCircle = generator(vector.point_2d(6, -2))
        self._middle: plate.PlateCircle = plate_factory.make(
            1, 0.75, vector.point_2d(0, -0.75)
        )

        self._line = plate.plate_circle_tangent_line(self._left, self._right)

        self.add(
            self._middle.inside,
            self._middle.middle,
            self._left.get_group(),
            self._right.get_group(),
            self._line.get_group(),
        )
        title.reset()

    def construct(self):
        self.play(title.next("Add outer circle"))
        self.play(mn.GrowFromCenter(self._middle.outside))

        self.play(title.next("Redraw boundary"))
        self.play(mn.Uncreate(self._line))
        self.wait(0.5)
        self.play(mn.Create(plate.plate_circle_tangent_line(self._left, self._middle)))
        self.play(mn.Create(plate.plate_circle_tangent_line(self._middle, self._right)))

        self.wait(animation.END_DELAY)


class BoundaryConstraintScene(mn.Scene):
    def setup(self):
        generator = plate_factory.make_generator(1.75, 0.75)
        self._left: plate.PlateCircle = generator(vector.point_2d(-6, -2))
        self._right: plate.PlateCircle = generator(vector.point_2d(6, -2))
        self.add(self._left.get_group(), self._right.get_group())

        self._tangent_points: tuple[vector.Point2d, vector.Point2d] = (
            plate.plate_circle_tangent_points(self._left, self._right)
        )

        left_start_point = self._tangent_points[0] + vector.point_2d(1.75, 0.75)
        right_start_point = self._tangent_points[1] + vector.point_2d(-2, 0.5)

        self._line = sketch.make_line(left_start_point, right_start_point)
        title.reset()

    def construct(self):
        self.play(title.next("Create line"))
        self.play(mn.Create(self._line))

        self.play(title.next("Add coincident constraints"))
        self.play(constraint.Coincident(self._line.start, self._left))
        self.play(constraint.Coincident(self._line.end, self._right))

        self.play(title.next("Add tangent constraints"))
        self.play(constraint.Tangent(self._line, self._left, rotate=True))
        self.play(
            constraint.Tangent(self._line, self._right, rotate=True, reverse=True)
        )

        self.wait(animation.END_DELAY)
