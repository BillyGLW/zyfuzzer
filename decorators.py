import ast

def arg_parse(w_func):
	def wrapper(*args, **kwargs):
		_args = []
		assert args[2]
		for arg in args[2]:
			if (type(arg) == int):
				_args.append(ast.Num(arg))
			elif (type(arg) == str):
				_args.append(ast.Str(arg))
			elif (type(arg) == bytes):
				_args.append(ast.Bytes(arg))
		args[2].clear()
		args[2].append(_args)
		return w_func(*args, **kwargs)
	return wrapper
