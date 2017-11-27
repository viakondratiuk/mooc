import socket
import threading

db = {}


def process_request(conn, addr):
	# print("connected client:", addr)
	with conn:
		while True:
			try:
				req = conn.recv(1024).decode("utf8").strip()
			except socket.timeout:
				break

			resp = _get_response(req)
			conn.send(resp.encode("utf8"))


def run_server(host, port):
	with socket.socket() as sock:
		sock.bind((host, port))
		sock.listen(socket.SOMAXCONN)
		
		while True:
			conn, addr = sock.accept()
			conn.settimeout(30)
			th = threading.Thread(target=process_request, args=(conn, addr))
			th.start()


def put(req):
	key, value, timestamp = req

	if key not in db:
		db[key] = []
	db[key].append((value, timestamp))
	
	return "ok\n\n"


def get(req):
	key = req[0]
	resp = "ok\n"

	if key == "*":
		for key, items in db.items():
			for item in items:
				value, timestamp = item
				resp += "{} {} {}\n".format(key, value, timestamp)
	else:
		data = db.get(key, "")
		for item in data:
			value, timestamp = item
			resp += "{} {} {}\n".format(key, value, timestamp)
	

	return resp + "\n"


def _get_response(req):
	key, *data = req.split()

	if key == "put":
		resp = put(data)
	elif key == "get":
		resp = get(data)
	else:
		resp = "error\nwrong command\n\n"

	return resp


if __name__ == "__main__":
	run_server("127.0.0.1", 10001)