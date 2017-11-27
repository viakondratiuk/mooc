from multiprocessing import Process


def f(name):
	print("hello", name)

p = Process(target=f, args=("Bob",))
p.start()
p.join()