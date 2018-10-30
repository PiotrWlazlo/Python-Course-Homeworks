# -*- coding: utf-8 -*-
import unittest
import copy

class TestMethods(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(4),24)
        self.assertEqual(factorial(5),120)
    def test_fibonacci(self):
        self.assertEqual(fibonacci(10),55)
        self.assertEqual(fibonacci(11),89)
    def test_odwracanie(self):
        L = [2,5,1,6,4,10,14]
        L1 = copy.copy(L) #Gdyż lista zostaje nadpisana
        L2 = copy.copy(L)
        L3 = copy.copy(L)
        self.assertEqual(odwracanie_iter(L1,2,5),[2,5,10,4,6,1,14])
        self.assertEqual(odwracanie_iter(L,3,6),[2,5,1,14,10,4,6])
        self.assertEqual(odwracanie_rec(L2,2,5),[2,5,10,4,6,1,14])
        self.assertEqual(odwracanie_rec(L3,3,6),[2,5,1,14,10,4,6])
    def test_sum_sequence(self):
        seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
	self.assertEqual(sum_sequence(seq),45)
	def test_flatten(self):
	self.assertEqual(flatten(seq),[1, 2, 3, 4, 5, 6, 7, 8, 9])

#4.2   
def miarka(length):
	pattern = "....|"
	linear = ['|', '0']

	linear[0] += (pattern * length)
	for i in range(length):
		linear[1] += "%5s" % (i+1)

	output = linear[0] + '\n' + linear[1]
	print(output)
	return output

def prostokat(x,y):
	def generate_line(length, pattern, last_char):
		line = ''
		line += pattern * length
		line += last_char + '\n'
		return line

	output = ''
	for i in range(y):
		output += generate_line(x, '+---', '+')
		output += generate_line(x, '|   ', '|')

	output += generate_line(x, '+---', '+')
	print(output)
	return output

#4.3
def factorial(n):
    result = 1
    for x in range(1,n+1):
        result *= x
    return result

#4.4
def fibonacci(n):
    if n==0: return 0
    if n==1: return 1
    x,y=0,1
    for i in range(1,n+1):
        r = x+y
        y = x
        x = r
    return r

#4.5
def odwracanie_iter(L,left,right):
    while(right>left):
        x = L[left]
        L[left] = L[right]
        L[right] = x
        right -= 1; left += 1
    return L

def odwracanie_rec(L,left,right):
    x = L[left]
    L[left] = L[right]
    L[right] = x
    if left+1 < right-1:
        odwracanie_rec(L,left+1,right-1)
    return L
    
#4.6
result = 0

def islist(sekw): return isinstance(sekw,list)
def istuple(sekw): return isinstance(sekw,tuple)

def sum_sequence(seq):
    global result
    for i in seq:
        if not islist(i) and not istuple(i):
            result += i
        else:
            sum_sequence(i)
    return result

#4.7
def flatten(seq):
	L = []
	for i in seq:
		if not islist(i) and not istuple(i):
			L.append(i)
		else:
			L += flatten(i)
	return L


if __name__ =='__main__':
    unittest.main()
    

