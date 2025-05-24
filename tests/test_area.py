import unittest
from area.circle import Circle
from area.triangle import Triangle
from area.any import compute_area


class TestArea(unittest.TestCase):
    def test_circle_area(self):
        c = Circle(1)
        self.assertAlmostEqual(c.area(), 3.14159, places=4)

    def test_triangle_area(self):
        t = Triangle(3, 4, 5)
        self.assertAlmostEqual(t.area(), 6.0)

    def test_triangle_invalid(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 10)

    def test_triangle_right_angled(self):
        t = Triangle(3, 4, 5)
        self.assertTrue(t.is_right_angled())

    def test_any_area(self):
        t = Triangle(3, 4, 5)
        c = Circle(1)
        self.assertAlmostEqual(compute_area(t), 6.0)
        self.assertAlmostEqual(compute_area(c), 3.14159, places=4)


if __name__ == '__main__':
    unittest.main()
