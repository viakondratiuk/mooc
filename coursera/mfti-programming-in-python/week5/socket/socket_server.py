import socket
import threading


# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.bind(("127.0.0.1", 10001))
# sock.listen(socket.SOMAXCONN)

# conn, addr = sock.accept()
# while True:
# 	data = conn.recv(1024)
# 	if not data:
# 		break
# 	print(data.decode("utf8"))
# conn.close()
# sock.close()

# context manager

# with socket.socket() as sock:
# 	sock.bind(("127.0.0.1", 10001))
# 	sock.listen(socket.SOMAXCONN)

# 	while True:
# 		conn, addr = sock.accept()
# 		with conn:
# 			while True:
# 				data = conn.recv(1024)
# 				if not data:
# 					break
# 				print(data.decode("utf8"))

# several connections threading
def process_request(conn, addr):
	print("connected client:", addr)
	with conn:
		while True:
			data = conn.recv(1024)
			if not data:
				break
			print(data.decode("utf-8"))

with socket.socket() as sock:
	sock.bind(("", 10001))
	sock.listen(socket.SOMAXCONN)
	while True:
		conn, addr = sock.accept()
		th = threading.Thread(target=process_request, args=(conn, addr))
		th.start()