from threading import Thread


def f(name):
	print("hello", name)

th = Thread(target=f, args=("Bob",))
th.start()
th.join()
