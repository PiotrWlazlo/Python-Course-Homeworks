from priority_queue_python import PriorityQueue as PriorityQueuePython
from priority_queue import PriorityQueue
import unittest


class TestStack(unittest.TestCase):

    def setUp(self):
        self.pq = PriorityQueue(5)
        self.pq1 = PriorityQueuePython()
        self.pq2 = PriorityQueue(1)
        self.pq2.insert(1)

    def test_init(self):
        self.tmp = PriorityQueue(5)
        self.assertEqual(self.tmp.size, 5)
        self.assertEqual(self.tmp.n, 0)
        self.assertEqual(len(self.pq1.items), 0)

    def test_is_empty(self):
        self.assertTrue(self.pq.is_empty())
        self.assertFalse(self.pq2.is_empty())
        self.assertTrue(self.pq1.is_empty())

    def test_is_full(self):
        self.assertFalse(self.pq.is_full())
        self.assertTrue(self.pq2.is_full())

    def test_insert(self):
        self.pq.insert(2)
        self.pq.insert(5)
        self.assertEqual(2, self.pq.n)
        self.assertEqual(1, self.pq2.n)
        with self.assertRaises(ValueError):
            self.pq2.insert(2)

    def test_remove(self):
        self.pq.insert(2)
        self.pq.insert(5)
        self.assertEqual(self.pq2.remove(), 1)
        self.assertEqual(self.pq.remove(), 5)
        self.assertEqual(self.pq.remove(), 2)
        with self.assertRaises(ValueError):
            self.pq2.remove()
            self.pq1.remove()
            self.pq.remove()

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
