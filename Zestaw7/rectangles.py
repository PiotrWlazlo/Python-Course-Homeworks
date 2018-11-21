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

    def test_intersection(self):
        self.assertTrue(self.rect1.intersect(self.rect2), True)
        self.assertEqual(self.rect1.intersection(self.rect2), self.rect1)
        self.assertFalse(self.rect1.intersection(Rectangle(-5, -5, -1, -1)), False)

    def test_cover(self):
        self.assertEqual(self.rect1.cover(self.rect2), self.rect2)
        self.assertEqual(self.rect2.cover(Rectangle(5, 6, 7, 8)), Rectangle(-1, -2, 7, 8))

    def test_make4(self):
        self.assertEqual(self.rect1.make4(), [Rectangle(2, 2, 3.5, 3.5),
                                              Rectangle(2, 3.5, 3.5, 5),
                                              Rectangle(3.5, 2, 5, 3.5),
                                              Rectangle(3.5, 3.5, 5, 5)])

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        # Chcemy, aby x1 <= x2, y1 <= y2.
        if x2 < x1:
            raise ValueError("x2 jest mniejsze od x1")
        if y2 < y1:
            raise ValueError("y2 jest mniejsze od y1")

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

    def intersection(self, other):  # część wspólna prostokątów
        if self.intersect(other):
            x1 = max(self.pt1.x, other.pt1.x)
            y1 = max(self.pt1.y, other.pt1.y)
            x2 = min(self.pt2.x, other.pt2.x)
            y2 = min(self.pt2.y, other.pt2.y)

            return Rectangle(x1, y1, x2, y2)
        else:
            return False

    def cover(self, other):  # prostąkąt nakrywający oba
        x1 = min(self.pt1.x, other.pt1.x)
        y1 = min(self.pt1.y, other.pt1.y)
        x2 = max(self.pt2.x, other.pt2.x)
        y2 = max(self.pt2.y, other.pt2.y)

        return Rectangle(x1, y1, x2, y2)

    def make4(self):  # zwraca listę czterech mniejszych
        x1 = self.pt1.x
        x2 = self.pt2.x
        y1 = self.pt1.y
        y2 = self.pt2.y
        dx = (x1 + x2) / 2.0
        dy = (y1 + y2) / 2.0

        return [Rectangle(x1, y1, dx, dy),
                Rectangle(x1, dy, dx, y2),
                Rectangle(dx, y1, x2, dy),
                Rectangle(dx, dy, x2, y2)]

    def intersect(self, other):
        if self.pt1.x > other.pt2.x or other.pt1.x > self.pt2.x:
            return False
        if self.pt1.y > other.pt2.y or self.pt2.y < other.pt1.y:
            return False
        return True

if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
