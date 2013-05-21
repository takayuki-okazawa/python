import time
import hashlib
import pickle

cache = {}

def is_obsolete(entry, duration):
	return time.time() - entry['time'] > duration

def compute_key(function, args, kw):
	key = pickle.dumps((function.func_name, args, kw))
	return hashlib.sha1(key).hexdigest()

def memoize(duration=10):
	def _memoize(function):
		def __memoize(*args, **kw):
			key = compute_key(function, args, kw)
			print(cache)
			if key in cache and not is_obsolete(cache[key], duration):
				print('Cache')
				return cache[key]['value']

			print('No Cache')
			result = function(*args, **kw)
			cache[key] = {'value':result, 'time':time.time()}
			return result
		return __memoize
	return _memoize



#test
@memoize()
def hoge(a, b):
	return a+b

hoge(1,2)
hoge(1,2)
hoge(1,3)