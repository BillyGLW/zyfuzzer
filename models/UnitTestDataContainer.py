import uuid
import re
import astor, ast
from api.ast_api import AST_API
from misc import FUZZ_DIR, UNIT_TESTS_DIR
from copy import copy, deepcopy
import code

class UnitTestDataContainer(AST_API):
	def __init__(self, _test_case_filename):
		self.test_case_filename = _test_case_filename
		self.uuid    = uuid.uuid1()
		self.ast     = ast.parse(open(UNIT_TESTS_DIR + self.test_case_filename, "r").read())
		self.source_code = astor.to_source(self.ast)
		self.defined_classes = self.classes_from_ast(self.ast)
		self.parsed_class_dict = self.functions_parse(self.defined_classes)
		self.functions_transformed = self.function_transform_from_ast(self.defined_classes)
		self.fuzzed_ast = self.fuzz_ast(self.functions_transformed)

	def get_params_func_name(self, src):
		# TODO: refactor regex, so that stripping wont be needed
		test_name = re.findall(r"def (.*?)\(", src)[0]
		func_name_pattern = r"assert[\w]*\((.*?)\("
		assert_type = re.findall(r"self\.([\w]+)\(", src)[0]
		func_name = re.findall(func_name_pattern, src)[0]
		params_pattern =  func_name + r"\((.*?)\)"
		predicted_val = re.findall(r"\)\,[\w]*(.*?)\)", src)[0].strip()
		params = list(map(lambda x: x.strip(), re.findall(params_pattern, src)[0].split(",")))
		return params, predicted_val, func_name, test_name, assert_type 

	def functions_parse(self, obj):	
		'''
		Returns dict of function names and its parameters of an parsed class. 
		_ast.ClassDef object
		Format:
		{testname: [func_name, [param1, param2]]}
		real-world:
		{'test_addition_odd': ['wa.add', ['3', ' 5']]}
		'''
		dict_parsed = {}
		for _class in obj:
			for func in _class.body:
				_ = astor.to_source(func)
				params, predicted_val, func_name, test_name, assert_type = self.get_params_func_name(_)
				dict_parsed[test_name] = [assert_type, func_name, predicted_val, params]
		return dict_parsed


	def function_transform_from_ast(self, obj, _oldfunc="assert", _newfunc="cmp", mutate=False):	
		'''
		Modify structure of ast block. 
		Searching through function definitions for eg. assert then replace with eg. cmp. (with function syntax rules).
		'''
		class_expressions_dict = {}
		for _class in obj:
			for _func in _class.body:
				class_expressions_dict[_func.name] = list()
				for expr in _func.body:
					if _oldfunc in astor.to_source(expr):
						cmp_arg = "{0}({1}({2}), {3})".format(
							_newfunc,
							self.parsed_class_dict[_func.name][1], 
							','.join(self.parsed_class_dict[_func.name][3]), 
							self.parsed_class_dict[_func.name][2])
						assert_to_arg = self.gen_expr_from_string(cmp_arg)
						class_expressions_dict[_func.name].append(assert_to_arg) 
					else:
						class_expressions_dict[_func.name].append(expr) 
		return class_expressions_dict

	def classes_from_ast(self, ast):
		'''
		Returns classes avaible in module. (_ast.Module object)
		'''
		classes = []
		for node in ast.body:
			if "ClassDef" in node.__str__():
				classes.append(node)
		return classes


	def fuzz_ast(self, functions_transformed):
		'''
		TODO: Traverse through AST (will be similar to/function_parse/) and by modyfing src code 
				create own environment.
		'''
		tmp_ast = deepcopy(self.ast)
		for _class in tmp_ast.body:
			if "Class" in str(_class):
				for _func in _class.body:
						if _func.name in functions_transformed:
							generated = self.gen_block_TryExcept(functions_transformed[_func.name], [self.gen_expr_from_string("print(1)")])
							_func.body = [generated]
		return tmp_ast

