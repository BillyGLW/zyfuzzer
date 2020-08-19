
def fuzzed_unit_test():
	try:
		x = SUT.func("test1#fuzzing")
		cmp("test2", x)

	except(Exception, e):
		self.assertEquals(type(e), StandardException)
  
