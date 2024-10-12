import math
from animations.geometry import vector


def circle_to_circle_tangent(
    center1: vector.Point2d, radius1: float, center2: vector.Point2d, radius2: float
) -> tuple[vector.Point2d, vector.Point2d]:
    """
    Returns the outer tangent line between two circles.
    The tangent is such that it is on the (left) outside of 1 and 2 when they are arranged in clockwise fashion.
    To flip the tangent, flip the order of the circles.
    """
    dist = vector.norm(center2 - center1)
    delta = (center2 - center1) / dist
    cross = vector.point_2d(-delta[1], delta[0])
    alpha = (radius1 - radius2) / dist
    beta = (1 - alpha**2) ** 0.5
    return (
        center1 + (alpha * delta + beta * cross) * radius1,
        center2 + (alpha * delta + beta * cross) * radius2,
    )


def point_to_circle_tangent(
    point: vector.Point2d, center: vector.Point2d, radius: float
) -> vector.Point2d:
    """
    Returns the outer tangent line between a circle and a point.
    The tangent is such that it is on the outside when point is clockwise to center.
    To flip the tangent, pass point before center.
    """
    # if not reverse:
    #     radius *= -1

    dist = vector.norm(point - center)
    angle = math.acos(radius / dist)
    angle_offset = math.atan2(point[1] - center[1], point[0] - center[0])
    return vector.point_2d(
        center[0] + radius * math.cos(angle_offset - angle),
        center[1] + radius * math.sin(angle_offset - angle),
    )


def circle_to_point_tangent(
    center: vector.Point2d, radius: float, point: vector.Point2d
) -> vector.Point2d:
    return point_to_circle_tangent(point, center, -radius)
