"""
Модуль для вычисления площади любой фигуры.

Функция `compute_area` принимает объект, реализующий интерфейс Shape,
и вызывает его метод `area()` для получения площади.

Обеспечивает вычисление площади без знания конкретного типа фигуры
в момент компиляции (compile-time).
"""

from typing import Union
from .circle import Circle
from .triangle import Triangle
from .base import Shape


def compute_area(shape: Shape) -> float:
    return shape.area()
