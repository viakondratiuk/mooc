
class File:

	def __init__(self, path):
		self.path = path

	def write(self, data):
		with open(self.path, "a") as f:
			f.write(data)

	def __add__(self, other):
		pass

	def __iter__(self):
		return self

	def __next__(self):
		pass

	def __str__(self):
		print(self.path)


if __name__ == "__main__":
	obj = File("/tmp/file.txt")
	obj.write("line\n")

	# first = File("/tmp/first")
	# second = File("/tmp/secons")

	# new_obj = first + second

	# for line in File("/tmp/file.txt"):
	# 	print(line)

	# assert print(obj) == "/tmp/file.txt"
