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


def parse(parsed_obj):
	pass

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
	un_f = get_unit_tests()
	api = a_api()
	test_case = UnitTestDataContainer(un_f[0])
	zyfuzzer = ZyFuzzer(test_case)

	base_code = test_case.defined_classes
	print_interesting_info(base_code)

	parsed_dict = test_case.parsed_class_dict
	parsed_code = test_case.source_code


	x = zyfuzzer.gen_query_generator("wtfis that for", 20)
	print(list(x))
	# dct = locals()
	# for k in list(globals()):
 #  		dct[k] = globals()[k]
	# code.InteractiveConsole(dct).interact()


	# TODO: refactorize that line 109-110
	# testcase_filename = "{}_{}".format("fuzz", str(round(time()))[2:9])
	
	# with open(FUZZ_DIR + testcase_filename, "w") as f:
	# 	f.write(parsed_code)

	# params = ''.join([INTERPRETER, FUZZ_DIR, testcase_filename])
	# proc = subprocess.Popen(params, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	# stdout_data = proc.communicate()
	# print(stdout_data)

if __name__ == "__main__":
	main()