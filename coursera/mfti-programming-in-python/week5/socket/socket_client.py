import socket

# long

# sock = socket.socket()
# sock.connect(("127.0.0.1", 10001))
# sock.sendall("ping".encode("utf8"))
# sock.close()

# short

# sock = socket.create_connection(("127.0.0.1", 10001))
# sock.sendall("ping".encode("utf8"))
# sock.close()

# context manager
with socket.create_connection(("127.0.0.1", 10001)) as sock:
	sock.sendall("ping".encode("utf8"))
