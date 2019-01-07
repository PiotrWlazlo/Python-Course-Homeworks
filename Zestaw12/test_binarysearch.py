import unittest
import random
from BinarySearch_rec import *

class TestBinarySearch(unittest.TestCase):
    def test(self):
        l = [1,5,8,12,15,17,19,21,27,29,30,14,23]
        self.assertEqual(binary_search_recursion(l,0,len(l)-1,15),4)
        self.assertEqual(binary_search_recursion(l,0,len(l)-1,21),7)
        self.assertEqual(binary_search_recursion(l,0,len(l)-1,151),None)
            
if __name__ == '__main__':
    unittest.main()
