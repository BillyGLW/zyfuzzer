import subprocess
import os
from misc import RADAMSA_PATH

import random
import code

class PyRadamsa(object):
	"""docstring for pyradamsa"""
	def __init__(self):
		super(PyRadamsa, self).__init__()



	def gen_query_generator(self, _query, _loops, _from=0):
		assert type(_loops) == int 
		for i in range(_from, _loops):
			yield self.single_query(_query, i)



	def gen_query_list(self, _params_to_mutate, _seed=1):
		assert type(_params_to_mutate) == list
		mutated_params = []
		for param_value in _params_to_mutate:
			mutated_params.append(str(self.single_query(param_value, _seed), "utf-8", "ignore"))

		return mutated_params

	def single_query(self, _query, _seed):
		assert type(_seed) == int
		_query = "echo \"{0}\" | {1} --seed {2}".format(_query, RADAMSA_PATH, _seed)
		try:
			proc = subprocess.Popen(_query, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
			stdout_data = proc.communicate(timeout=15)
		except TimeoutExpired:
			proc.kill()
			outs, errs = proc.communicate()
		return (stdout_data[0])
		# dct = locals()
		# for k in list(globals()):
	 #  		dct[k] = globals()[k]
		# code.InteractiveConsole(dct).interact()



