import unittest
from lib import Circle,Rectangle,Square,Triangle

class TestGeometry(unittest.TestCase):

    def test_circle_area(self):
        circle = Circle.Circle(5)
        self.assertAlmostEqual(circle.area(), 78.54, places=2)

    def test_circle_area_with_negative_radius(self):
        with self.assertRaises(ValueError):
            circle = Circle.Circle(-3)
            circle.area()

    def test_rectangle_perimeter(self):
        rectangle = Rectangle.Rectangle(2000000, 2000000)
        self.assertEqual(rectangle.perimeter(), 8000000)

    def test_rectangle_perimeter_with_invalid_type(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle.Rectangle("b", 5)
            rectangle.perimeter()

    def test_square_area_with_large_side(self):
        square = Square.Square(1000000)
        self.assertEqual(square.area(), 1000000000000)

    def test_triangle_area_with_negative_side(self):
        with self.assertRaises(ValueError):
            triangle = Triangle.Triangle(-5, 6, 7)
            triangle.area()

if __name__ == '__main__':
    unittest.main()
