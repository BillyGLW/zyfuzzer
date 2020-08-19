try:
	import os
	BASE_DIR = os.getcwd() 
except Exception as e:
	print(e)

FUZZ_DIR = BASE_DIR + "\\fuzzing_testcases\\"
INTERPRETER = "python "
separator = "\n" + (" " * 4)


def gen_sep(val):
	return (" " * val)