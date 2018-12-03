import unittest
from SingleList import *

class SingleListTest(unittest.TestCase):
    def setUp(self):
        self.node = Node(1)
        self.lista = SingleList(6,5,4,3,2,1)
        # self.lista.__init__(6, 5, 4, 3, 2, 1)

    def test_init(self):
        self.assertEqual(self.lista.__str__(), [1,2,3,4,5,6], "test_init error")

    def test_reverse(self):
        self.assertEqual(self.lista.reverse().__str__(), [6,5,4,3,2,1], "Test_reverse Error")