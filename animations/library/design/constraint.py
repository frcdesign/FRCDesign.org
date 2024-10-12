from typing import Any

import manim as mn

from library.design import sketch, sketch_animation
from library.math import vector, tangent
from library.utils.type_utils import not_none


class ConstraintBase(mn.Succession):
    def __init__(self, animation: mn.Animation | Any, *mobjects: sketch.Base) -> None:
        super().__init__(
            *[not_none(sketch_animation.Click(mobject)) for mobject in mobjects],
            animation,
        )


class Equal(ConstraintBase):
    def __init__(
        self, base: sketch.ArcBase | sketch.Line, target: sketch.ArcBase | sketch.Line
    ) -> None:
        if isinstance(base, sketch.ArcBase) and isinstance(target, sketch.ArcBase):
            animation = target.animate.set_radius(base.get_radius())
        elif isinstance(base, sketch.Line) and isinstance(target, sketch.Line):
            animation = base.equal_constraint(target)
        else:
            raise TypeError("Expected arguments to be of the same type.")
        super().__init__(animation, base, target)


class Coincident(ConstraintBase):
    def __init__(self, base: sketch.Point, target: sketch.Base) -> None:
        animation = base.animate.move_to(target.coincident_target(base.get_center()))
        super().__init__(animation, base, target)


class Concentric(ConstraintBase):
    def __init__(self, base: sketch.ArcBase | sketch.Point, target: sketch.ArcBase):
        animation = base.animate.move_to(target.concentric_target())
        super().__init__(animation, base, target)


class Tangent(ConstraintBase):
    def __init__(
        self,
        base: sketch.Line | sketch.ArcBase,
        target: sketch.ArcBase,
        rotate: bool = False,
        reverse: bool = False,
    ) -> None:
        if not rotate:
            translation = base.get_tangent_translation(target)
            animation = base.animate.shift(translation)
        else:
            if not isinstance(base, sketch.Line):
                raise TypeError("Cannot rotate an arc.")

            start = base.is_start_closer_to_target(target)
            close, far = (base.start, base.end) if start else (base.end, base.start)
            close_point, far_point = close.get_center(), far.get_center()

            if reverse:
                tangent_point = tangent.point_to_circle_tangent(
                    far_point, target.get_center(), target.get_radius()
                )
            else:
                tangent_point = tangent.circle_to_point_tangent(
                    target.get_center(), target.get_radius(), far_point
                )

            angle = vector.angle_between_points(
                close_point, tangent_point, target.get_center()
            ) * (-1 if reverse else 1)

            animation = close.animate(
                path_arc=angle, path_arg_centers=[target.get_center()]  # type: ignore
            ).move_to(tangent_point)

        super().__init__(animation, base, target)


class Align(ConstraintBase):
    def __init__(
        self,
        type: sketch.AlignType,
        line: sketch.Line | None = None,
        points: tuple[sketch.Point, sketch.Point] | None = None,
    ):
        if line is not None:
            super().__init__(line.align_constraint(type), line)
        elif points is not None:
            super().__init__(points[0].align_constraint(points[1], type), *points)
        else:
            raise ValueError("Expected either a line or two points.")


class Horizontal(Align):
    def __init__(
        self,
        line: sketch.Line | None = None,
        points: tuple[sketch.Point, sketch.Point] | None = None,
    ):
        return super().__init__(sketch.AlignType.HORIZONTAL, line=line, points=points)


class Vertical(Align):
    def __init__(
        self,
        line: sketch.Line | None = None,
        points: tuple[sketch.Point, sketch.Point] | None = None,
    ):
        return super().__init__(sketch.AlignType.VERTICAL, line=line, points=points)


class Midpoint(ConstraintBase):
    def __init__(
        self,
        base: sketch.Point,
        line: sketch.Line | None = None,
        points: tuple[sketch.Point, sketch.Point] | None = None,
    ) -> None:
        """Performs a midpoint constraint on the passed in points."""
        # setup click order
        if line is not None:
            args = [base, line]
        elif points is not None:
            args = [points[0], base, points[1]]
        else:
            # midpoint_constraint will throw
            args = []
        return super().__init__(
            base.midpoint_constraint(line=line, points=points), *args
        )
