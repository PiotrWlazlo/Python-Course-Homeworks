import math

class Point:
    """Klasa reprezentujaca punkty na plaszczyznie."""

    def __init__(self, x=0, y=0):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):  # zwraca string "(x, y)"
        return str("(" + str(self.x) + ", " + str(self.y) + ")")

    def __repr__(self):  # zwraca string "Point(x, y)"
        return str("Point(" + str(self.x) + ", " + str(self.y) + ")")

    def __eq__(self, other):  # obsluga point1 == point2
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __ne__(self, other):  # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny
        return (self.x * other.x) + (self.y * other.y)

    def cross(self, other):  # v1 x v2, iloczyn wektorowy 2D
        return self.x * other.y - self.y * other.x

    def length(self):  # dlugość wektora
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))
# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase):
    def setUp(self):
        self.pt1 = Point(2,2)
        self.pt2 = Point(5,6)
        self.pt3 = Point(7,8)
    def test_init(self):
        self.assertIsInstance(self.pt1,Point)
        self.assertIs(self.pt1.x,2)
        self.assertIs(self.pt1.y,2)

    def test_str(self):
        self.assertIsInstance(str(self.pt1), str)
        self.assertEqual(str(self.pt1), "(2, 2)")

    def test_repr(self):
        self.assertIsInstance(repr(self.pt1), str)
        self.assertEqual(repr(self.pt1), "Point(2, 2)")

    def test_eq(self):
        self.assertTrue(self.pt1 == Point(2, 2))
        self.assertFalse(self.pt1 == Point(0, 2))
        self.assertFalse(self.pt1 == Point(0, 0))

    def test_ne(self):
        self.assertTrue(self.pt1 != self.pt2)
        self.assertFalse(self.pt1 != Point(2, 2))

    def test_add(self):
        self.assertEqual(self.pt1 + self.pt2, self.pt3)
        self.assertEqual(self.pt1 + Point(-5, -2), Point(-3, 0))

    def test_sub(self):
        self.assertEqual(self.pt1 - self.pt2, Point(-3, -4))
        self.assertEqual(self.pt1 - self.pt3, Point(-5, -6))

    def test_mul(self):
        self.assertEqual(self.pt1 * self.pt2, 22)
        self.assertEqual(self.pt1 * self.pt3, 30)
        self.assertEqual(self.pt1 * Point(-5, -2), -14)

    def test_cross(self):
        self.assertEqual(self.pt1.cross(self.pt1), 0)
        self.assertEqual(self.pt1.cross(Point(0, 0)), 0)
        self.assertEqual(self.pt1.cross(self.pt2), 2)

    def test_length(self):
        self.assertEqual(Point(-5, 0).length(), 5)
        self.assertEqual(Point(0, 0).length(), 0)
        self.assertEqual(Point(3, 4).length(), 5)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
