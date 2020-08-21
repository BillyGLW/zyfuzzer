import ast
import astor
import subprocess

import os

import code

import re

from time import time

from misc import *

from api.ast_api import AST_API as a_api

from fuzzer import ZyFuzzer
from models.UnitTestDataContainer import UnitTestDataContainer


def get_unit_tests(_dir=UNIT_TESTS_DIR):
	'''
	Returns /string/ from test-cases .py file.
	'''
	file_list = []
	for item in os.listdir(_dir):
		if "unit" in item:
			file_list.append(item)
			break
	return file_list

def get_tests_info(ast):
	'''
	Returns classes avaible in module. (_ast.Module object)
	'''
	classes = []
	for node in ast.body:
		if "ClassDef" in node.__str__():
			classes.append(node)
	return classes

def print_interesting_info(classes_defined):
	contain_classes = len(classes_defined)
	found_unit_tests = 0
	unit_tests = []
	for i in classes_defined:
		found_unit_tests += len(i.body)
		unit_tests.append(i.body)

	print("[*] Found {} unit-tests classes.".format(contain_classes))
	print("[*] Found {} unit-tests methods.".format(found_unit_tests))


def main():
	# Set-up environment
	un_f = get_unit_tests()
	test_case = UnitTestDataContainer(un_f[0])
	zyfuzzer = ZyFuzzer(test_case)
	base_code = test_case.defined_classes

	# Print out test-case information
	print_interesting_info(base_code)

	zyfuzzer.run()

if __name__ == "__main__":
	main()