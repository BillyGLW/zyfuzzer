from misc import FUZZ_DIR

from api.radamsa_api import PyRadamsa

from time import time

from datetime import datetime, timedelta
import astor
class ZyFuzzer(PyRadamsa):
	def __init__(self, _cls_unit_model):
		super(ZyFuzzer, self).__init__()
		self.cls_unit_model = _cls_unit_model
		self.out_path = FUZZ_DIR
		self.testcase_filename = "{}_{}".format("fuzz", str(round(time()))[2:9])
		self.seed_value = 1
		self.time_started = datetime.now() 
		# maybe new enviroment?

	def run(self, hours_fuzzing=2):
		# modified testcase
		# exec
		# check if error
		# if error save it and INFORM! 
		# mutate for next
		# if no error
		# mutate()
		time_delta = timedelta(hours=hours_fuzzing)
		time_end = self.time_started + time_delta
		
		while (1):
			if (self.time_started > time_end):
				print("time is over.. exiting..")
				break
			try:
				self.mutate()
				# source passed, save unit-test
				testcase_filename = "{}_{}".format("fuzz", str(round(time()))[2:9])
				with open(FUZZ_DIR + testcase_filename, "w") as f:
					f.write(astor.to_source(self.cls_unit_model.fuzzed_ast))
				# shell execiute new testcase
				params = ''.join([INTERPRETER, FUZZ_DIR, testcase_filename])
				proc = subprocess.Popen(params, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
			except Exception as e:
				print(e)
		return


	def mutate(self):
		for item, value in self.cls_unit_model.parsed_class_dict.items():
			_mutated_params = super().gen_query_list(value[3], self.seed_value)
			# super() call init ?			
			self.cls_unit_model.parsed_class_dict[item][3] = _mutated_params
			self.cls_unit_model.functions_transformed = self.cls_unit_model.function_transform_from_ast(self.cls_unit_model.defined_classes)
			
			self.cls_unit_model.fuzz_ast(self.cls_unit_model.functions_transformed)
			# todo; include randomness into the seed value:
			self.seed_value += 1


		print(astor.to_source(self.cls_unit_model.fuzzed_ast))
		print(_mutated_params)
		# radamsa, bleb bindings?
		pass

	def code_transform(self):
		# calls to ast_api, then mutate call?
		pass
		


