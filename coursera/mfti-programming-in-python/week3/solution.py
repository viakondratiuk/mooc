
class FileReader():

	def __init__(self, path):
		self.path = path

	def read(self):
		try:
			with open(self.path, "r") as f:
				return f.read()
		except IOError:
			return ""


if __name__ == "__main__":
	reader = FileReader("../week2/to_json.py")
	ret = reader.read()
	print(ret)
