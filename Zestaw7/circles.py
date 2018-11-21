from points import Point
import math
import unittest


class TestCircle(unittest.TestCase):

    def setUp(self):
        self.tmp1 = Circle(-1, -1, 1)
        self.tmp2 = Circle(2, 0, 2)

    def test_init(self):
        self.assertEqual(self.tmp1.pt, Point(-1, -1))
        self.assertEqual(self.tmp1.pt.x, -1)
        self.assertEqual(self.tmp1.pt.y, -1)
        self.assertEqual(self.tmp1.radius, 1)
        with self.assertRaises(ValueError):
            Circle(0, 0, -1)

    def test_repr(self):
        self.assertEqual(repr(self.tmp1), "Circle(-1, -1, 1)")

    def test_eq(self):
        self.assertFalse(self.tmp1 == Circle(1, 20, 4))
        self.assertTrue(self.tmp1 == Circle(-1, -1, 1))
        self.assertTrue(self.tmp1 == Circle(-1.0, -1, 1.000))

    def test_ne(self):
        self.assertTrue(self.tmp1 != Circle(1, -1, 4))
        self.assertFalse(self.tmp1 != Circle(-1.0, -1, 1))
        self.assertFalse(self.tmp1 != Circle(-1, -1, 1))

    def test_area(self):
        self.assertEqual(self.tmp1.area(), math.pi * 1)
        self.assertEqual(self.tmp2.area(), math.pi * 4)

    def test_move(self):
        self.assertEqual(self.tmp1.move(1, 2), Circle(0, 1, 1))
        self.assertEqual(self.tmp2.move(3, 3), Circle(5, 3, 2))

    def test_cover(self):
        self.assertEqual(self.tmp2.cover(Circle(2, 0, 1)), Circle(2, 0, 2))
        self.assertEqual(Circle(-5, 0, 2).cover(Circle(4, 0, 2)), Circle(-0.5, 0, 6.5))

    def tearDown(self): pass


class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):  # "Circle(x, y, radius)"
        return "Circle(" + str(self.pt.x) + ", " + str(self.pt.y) + ", " + str(self.radius) + ")"

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):  # pole powierzchni
        return math.pi * self.radius * self.radius

    def move(self, x, y):  # przesuniecie o (x, y)
        self.pt.x += x
        self.pt.y += y
        return self

    def cover(self, other):  # okrąg pokrywający oba
        dist = (math.sqrt((self.pt.x - other.pt.x)**2 + (self.pt.y - other.pt.y)**2))

        if dist <= abs(self.radius - other.radius):
            if self.radius > other.radius:
                return self
            return other
        else:
            new_x = (self.pt.x + other.pt.x) / 2.0
            new_y = (self.pt.y + other.pt.y) / 2.0

            new_radius = dist / 2.0 + max(self.radius, other.radius)

        return Circle(new_x, new_y, new_radius)

if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
