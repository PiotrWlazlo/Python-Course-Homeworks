import unittest
from bucketsort import *
import copy


class TestBucketSort(unittest.TestCase):
    def test_random_ints(self):
        a = random_ints(100)
        a_s = copy.copy(a)
        a2 = random_ints(1000)
        a2_s = copy.copy(a2)
        a_s.sort()
        a2_s.sort()
        self.assertEqual(bucketsort(a), a_s, "random_ints_error")
        self.assertEqual(bucketsort(a2), a2_s,"random_ints_error")

    def test_almost_random_ints(self):
        b = almost_sorted_ints(100)
        b_s = copy.copy(b)
        b2 = almost_sorted_ints(1000)
        b2_s = copy.copy(b2)
        b_s.sort()
        b2_s.sort()
        self.assertEqual(bucketsort(b), b_s, "almost_random_ints_error")
        self.assertEqual(bucketsort(b2), b2_s, "almost_random_ints_error")

    def test_invert_almost_random_ints(self):
        c = invert_almost_sorted_ints(100)
        c_s = copy.copy(c)
        c2 = invert_almost_sorted_ints(1000)
        c2_s = copy.copy(c2)
        c_s.sort()
        c2_s.sort()
        self.assertEqual(bucketsort(c), c_s, "invert_almost_random_ints_error")
        self.assertEqual(bucketsort(c2), c2_s, "invert_almost_random_ints_error")

    def test_gauss_floats(self):
        d = gauss_floats(100)
        d_s = copy.copy(d)
        d2 = gauss_floats(1000)
        d2_s = copy.copy(d2)
        d_s.sort()
        d2_s.sort()
        self.assertEqual(neg_bucketsort(d), d_s, "gaus_floats_error")
        self.assertEqual(neg_bucketsort(d2), d2_s, "gaus_floats_error")

    def test_random_k_ints(self):
        e = random_k_ints(100)
        e_s = copy.copy(e)
        e2 = random_k_ints(1000)
        e2_s = copy.copy(e2)
        e_s.sort()
        e2_s.sort()
        self.assertEqual(bucketsort(e), e_s, 'random_k_ints_error')
        self.assertEqual(bucketsort(e2), e2_s, 'random_k_ints_error2')


if __name__ == '__main__':
    unittest.main()
