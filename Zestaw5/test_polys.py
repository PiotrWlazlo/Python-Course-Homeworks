import unittest
from polys import *


class TestPolynomials(unittest.TestCase):
    def setUp(self):
        self.p1 = [0,1]
        self.p2 = [0,0,1]
    def test_add_poly(self):
        self.assertEqual(add_poly(self.p1,self.p2),[0,1,1])
    def test_sub_poly(self):
        self.assertEqual(sub_poly(self.p1,self.p2),[0,-1,1])
    def test_mul_poly(self):
        self.assertEqual(mul_poly([1,3,5,7],[2,4,6]),[2,10,28,52,58,42])
    def test_is_zero(self):
        self.assertTrue(is_zero([0,0]))
        self.assertTrue(is_zero([0,0,0,0]))
        self.assertFalse(is_zero([0,1,2]))
        self.assertFalse(is_zero([2,2,1]))
    def test_cmp_poly(self):
        self.assertTrue(cmp_poly([1,2,5,0],[1,2,5,0]))
        self.assertTrue(cmp_poly([2,5,1],[2,5,1]))
        self.assertFalse(cmp_poly([3,7,1],[4,1,9,7]))
        self.assertFalse(cmp_poly([0,0,2],[4,1]))
    def test_eval_poly(self):
        self.assertEqual(eval_poly([-1, 2, -6, 2], 3), 5)
    def test_combine_poly(self):
        self.assertEqual(combine_poly([2, 1, 2], [0, 3]), [2, 3, 18])
    def test_pow_poly(self):
        self.assertEqual(pow_poly([-5, 1, 5], 3), [-125, 75, 360, -149, -360, 75, 125])
    def test_diff_poly(self):
        self.assertEqual(diff_poly([-5, 12, -4, 3]), [12, -8, 9])
        self.assertEqual(diff_poly([10, 20, 30, 40]), [20, 60, 120])
        self.assertEqual(diff_poly([-5, -12, -4.5, -3]), [-12, -9, -9])


if __name__ == '__main__':
    unittest.main()
