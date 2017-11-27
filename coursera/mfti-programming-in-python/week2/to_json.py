import functools
import json


def to_json(func):
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		return json.dumps(func(*args, **kwargs))
	return wrapper

@to_json
def get_data(a, b):
	return {"data": 42, "aa": 43}

# get_data = to_json(get_data)
# print(get_data(1, 2))