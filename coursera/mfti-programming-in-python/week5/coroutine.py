def grep(pattern):
	print("start grep")
	while True:
		line = yield
		if pattern in line:
			print(line)

def grep_python_coroutine():
	g = grep("python")
	yield from g

g = grep_python_coroutine()
print(g)
g.send(None)
g.send("golang is good")
g.send("python is better")