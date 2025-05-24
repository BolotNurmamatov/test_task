from typing import Union
from .circle import Circle
from .triangle import Triangle
from .base import Shape


def compute_area(shape: Shape) -> float:
    return shape.area()
