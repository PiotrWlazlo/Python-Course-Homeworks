from points import Point


class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):  # "[(x1, y1), (x2, y2)]"
        return str("[" + str(self.pt1) + ", " + str(self.pt2) + "]")

    def __repr__(self):  # "Rectangle(x1, y1, x2, y2)"
        return str("Rectangle(" + str(self.pt1.x) + ", " + str(self.pt1.y) +
                   ", " + str(self.pt2.x) + ", " + str(self.pt2.y) + ")")

    def __eq__(self, other):  # obsługa rect1 == rect2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):  # obsługa rect1 != rect2
        return not self == other

    def center(self):  # zwraca środek prostokąta
        return Point((self.pt1.x + self.pt2.x) / 2.0, (self.pt1.y + self.pt2.y) / 2.0)

    def area(self):  # pole powierzchni
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    def move(self, x, y):  # przesunięcie o (x, y)
        self.pt1 = Point(self.pt1.x + x, self.pt1.y + y)
        self.pt2 = Point(self.pt2.x + x, self.pt2.y + y)
        return self

from points import Point

import unittest


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rect1 = Rectangle(2, 2, 5, 5)
        self.rect2 = Rectangle(-1, -2, 5, 6)

    def test_init(self):
        self.assertIsInstance(self.rect1, Rectangle)

    def test_str(self):
        self.assertIsInstance(str(self.rect1), str)
        self.assertEqual(str(self.rect1), "[(2, 2), (5, 5)]")

    def test_repr(self):
        self.assertIsInstance(repr(self.rect1), str)
        self.assertEqual(repr(self.rect1), "Rectangle(2, 2, 5, 5)")

    def test_eq(self):
        self.assertTrue(self.rect1 == Rectangle(2, 2, 5, 5))
        self.assertFalse(self.rect1 == self.rect2)

    def test_ne(self):
        self.assertTrue(self.rect1 != self.rect2)
        self.assertFalse(self.rect1 != Rectangle(2, 2, 5, 5))

    def test_center(self):
        self.assertEqual(self.rect1.center(), Point(3.5, 3.5))
        self.assertEqual(self.rect2.center(), Point(2, 2))

    def test_area(self):
        self.assertEqual(self.rect1.area(), 9)
        self.assertEqual(self.rect2.area(), 48)

    def test_move(self):
        self.assertEqual(self.rect1.move(-1, -1), Rectangle(1, 1, 4, 4))
        self.assertTrue(self.rect2.move(-5, 2) == Rectangle(-6, 0, 0, 8))


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
