import unittest

import sys
sys.path.insert(0, "..")

import worker_addition as wa

import os


class TestAdditionMethod(unittest.TestCase):

	def test_addition_odd(self):
		x = "somevalueto be whatever"
		print("test1")
		self.assertEqual(wa.add(3, 5), 8)

	def test_addition_even(self):
		self.assertEqual(wa.add(2, 4), 6)


class TestSubstractionMethod(unittest.TestCase):

	def test_substraction_odd(self):
		self.assertEqual(wa.sub(3, 5), -2)

	def test_substraction_even(self):
		self.assertEqual(wa.sub(4, 2), 2)

if __name__ == "__main__":
	unittest.main()
