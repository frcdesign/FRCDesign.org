"""
    A collection of semantic aliases for type hinting used throughout the library.
"""
from typing import cast, TypeAlias, Any

import manim as mn
import numpy as np

Vector: TypeAlias = Any
# For compatability with manim, a 2d vector is defined as 3d vector with its third coordinate equal to zero.
Vector2d: TypeAlias = Any
# Vector3d: TypeAlias = Any

Point: TypeAlias = Any
# For compatability with manim, a 2d point is defined as a 3d point with its third coordinate equal to zero.
Point2d: TypeAlias = Any
# Point3d: TypeAlias = Any

Direction: TypeAlias = Any
Direction2d: TypeAlias = Any
# Direction3d: TypeAlias = Any

# An angle in radians
Angle = float


def norm(vector: Point | Vector) -> float:
    """
    Returns the norm (length) of a vector.
    """
    return cast(float, np.linalg.norm(vector))


def normalize(vector: Vector) -> Direction:
    return mn.normalize(vector)


def dot(vector1: Vector, vector2: Vector) -> Vector:
    return np.dot(vector1, vector2)


def vector_2d(x: float, y: float) -> Vector2d:
    """A constructor for a vector2d."""
    return np.array([x, y, 0])


# def vector_3d(x: float, y: float, z: float) -> Vector3d:
#     """A constructor for a 3D vector."""
#     return np.array([x, y, z])


def point_2d(x: float, y: float) -> Point2d:
    """A constructor for a 2D point."""
    return np.array([x, y, 0])


# def point_3d(x: float, y: float, z: float) -> Point3d:
#     """A constructor for a 3D point."""
#     return np.array([x, y, z])


def direction(from_point: Point, to_point: Point) -> Direction:
    return normalize(to_point - from_point)


def direction_2d(x: float, y: float) -> Direction2d:
    """A constructor for a 2D direction."""
    return normalize(np.array([x, y, 0]))


# def direction_3d(x: float, y: float, z: float) -> Direction3d:
#     """A constructor for a 3D direction."""
#     return normalize(np.array([x, y, z]))


def angle_between_vectors(x1: Vector, x2: Vector) -> Angle:
    return mn.angle_between_vectors(x1, x2)


def angle_between_points(start: Point, end: Point, center: Point) -> Angle:
    return angle_between_vectors(start - center, end - center)


ZERO_LENGTH: float = 0.00001
ZERO_LENGTH_VECTOR: Vector2d = vector_2d(ZERO_LENGTH, ZERO_LENGTH)
