"""
Модуль для работы с треугольниками.

Содержит класс Triangle, который позволяет создавать объект треугольника
по трём сторонам, вычислять его площадь, а также проверять,
является ли треугольник прямоугольным.
"""

import math
from .base import Shape


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        self.a, self.b, self.c = a, b, c
        if not self._is_valid():
            raise ValueError("Invalid triangle sides")

    def _is_valid(self):
        a, b, c = self.a, self.b, self.c
        return a + b > c and a + c > b and b + c > a

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_angled(self) -> bool:
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[2] ** 2, sides[0] ** 2 + sides[1] ** 2)
