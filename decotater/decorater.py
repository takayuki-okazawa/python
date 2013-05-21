def hello(function):
	def _hello(*args, **kw):
		result = function(*args, **kw)
		return "Hello, {0}".format(result)
	return _hello

@hello
def name(arg):
	return arg

print name('Takayuki')