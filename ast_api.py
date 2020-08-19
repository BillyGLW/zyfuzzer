import ast

import code

from decorators import * 

class AST_API(object):
	"""0.01 AST_API - this version allows to operate on function, try, except, expressions."""
	def __init__(self):
		super(AST_API, self).__init__()

	@arg_parse
	def gen_func_Call(self, func, arguments):
		# dct = locals()
		# for k in list(globals()):
	 #  		dct[k] = globals()[k]
		# code.InteractiveConsole(dct).interact()
		_func = ast.Name(func, ast.Load())
		assert type(arguments) == list
		_fcall = ast.Call(_func, arguments, [])
		return (ast.Expr(_fcall))

	def gen_expr_from_string(self, data):
		_ = ast.parse(data)
		return (_.body[0])

	def gen_block_TryExcept(self, expr_try, expr_except):
		assert ((type(expr_try) and type(expr_except)) == list)
		# TODO: could be made in one-liner
		exception_handler = [ast.ExceptHandler(ast.Name("Exception", ast.Store()), "e", expr_except)] 
		tryExcept_block = ast.Try(expr_try, exception_handler, [], []) 
		return (tryExcept_block)


