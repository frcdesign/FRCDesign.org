from typing import TypeVar


T = TypeVar("T")


def not_none(value: T | None) -> T:
    if value is None:
        raise AssertionError("Unexpected null")
    return value


ALMOST_ZERO = 0.0000001
