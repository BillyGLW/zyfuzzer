import unittest
import sys
sys.path.insert(0, ".")

from api.radamsa_api import PyRadamsa


class TestRadamsaApi(unittest.TestCase):
	def test_gen_query_generator(self):
		radamsa_api = PyRadamsa()
		testcase_1 = radamsa_api.gen_query_generator("test", 2)
		self.assertEqual(str(type(testcase_1)), "<class 'generator'>")
		self.assertEqual(len(list(testcase_1)), 2)

	def test_seed_determinant(self):
		radamsa_api = PyRadamsa()
		testcase_1 = radamsa_api.single_query("hej", 2)
		testcase_2 = radamsa_api.single_query("hej", 2)
		self.assertEqual(testcase_1, testcase_2)

if __name__ == '__main__':
	unittest.main()