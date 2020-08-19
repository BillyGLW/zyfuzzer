try:
	import os
	BASE_DIR = os.getcwd() 
except Exception as e:
	print(e)

FUZZ_DIR = BASE_DIR + "\\tests\\fuzzing_test_cases\\"
UNIT_TESTS_DIR  = BASE_DIR + "\\tests\\unit_tests_cases\\"
INTERPRETER = "python "
separator = "\n" + (" " * 4)


def gen_sep(val):
	return (" " * val)