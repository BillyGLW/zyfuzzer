try:
	import os
	BASE_DIR = os.getcwd() 
except Exception as e:
	print(e)

FUZZ_DIR = os.path.join(BASE_DIR + "/tests/fuzzing_test_cases/")
UNIT_TESTS_DIR  = os.path.join(BASE_DIR + "/tests/unit_tests_cases/")
RADAMSA_PATH = os.path.join(BASE_DIR + "/radamsa_bin/", "radamsa")
INTERPRETER = "python "
separator = "\n" + (" " * 4)


def gen_sep(val):
	return (" " * val)