import time
import os

pid = os.fork()


if pid == 0:
	# child process
	while True:
		print("child: ", os.getpid())
		time.sleep(5)
else:
	# parent process
	print("parent: ", os.getpid())
	os.wait()
