# AST \ TRY BLOCK

### Step 1:

- Define excepthandler node eg. 
'''
e = [ast.ExceptHandler(ast.Name("x", ast.Store()), "y", [p])] 
'''

will be represented as:
'''
try:
    pass
except x as y:
    pass
'''

listing:
'''
In [42]: t = ast.Try([p], e, [], [])
In [43]: print(astor.to_source(t))
try:
    pass
except x as y:
    pass
'''

### Generally speaking
- mentioned definitions of building new nodes, basically just creates an expression (STRING!), if its restricted by "node rules" it will be able to pass the test.


### AIM

Done: 
-Able to represent following code:
```
def unit_test():
	x = SUT.func("test")
	self.assertEquals("test2", x)
```

-Into format below:
```
def fuzzed_unit_test():
	try:
		x = SUT.func("test1#fuzzing")
		cmp("test2", x)
	except(Exception, e):
		self.assertEquals(type(e), StandardException)

```


# Sources

https://www.programcreek.com/python/example/80495/ast.Try / Example 5/ but all of those are interesting

https://python-ast-explorer.com/ # online ast trees viewer

[![Build Status](https://travis-ci.com/BillyGLW/zyfuzzer.svg?branch=master)](https://travis-ci.com/BillyGLW/zyfuzzer)
