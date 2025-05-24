"""
Модуль для работы с кругами.

Содержит класс Circle, который позволяет создавать объект круга по радиусу
и вычислять его площадь.
"""

import math
from .base import Shape

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2