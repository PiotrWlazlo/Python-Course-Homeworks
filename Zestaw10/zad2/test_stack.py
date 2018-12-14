from stack import Stack
import unittest


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack(2)
        self.stack1 = Stack(1)
        self.stack1.push(1)
        self.stack2 = Stack()

    def test_init(self):
        self.tmp = Stack(5)
        self.assertEqual(self.tmp.size, 5)
        self.assertEqual(self.tmp.n, 0)
        self.assertEqual(self.stack.size, 2)

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.assertFalse(self.stack1.is_empty())
        self.assertTrue(self.stack2.is_empty())

    def test_is_full(self):
        self.assertFalse(self.stack.is_full())
        self.assertTrue(self.stack1.is_full())
        self.assertFalse(self.stack2.is_full())

    def test_push(self):
        self.stack.push(2)
        self.assertEqual(1, self.stack.n)
        self.assertEqual(1, self.stack1.n)
        self.assertEqual(1, self.stack1.items[0])
        with self.assertRaises(ValueError):
            self.stack1.push(2)

    def test_pop(self):
        self.assertEqual(self.stack1.pop(), 1)
        with self.assertRaises(ValueError):
            self.stack1.pop()
            self.stack2.pop()

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
