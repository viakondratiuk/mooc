import socket
import time


class ClientError(Exception):
	pass

class Client:

	def __init__(self, host, port, timeout=None):
		self.host = host
		self.port = port
		self.timeout = timeout
		self.socket = socket.create_connection((self.host, self.port), self.timeout)

	def _read(self):
		data = b""

		while not data.endswith(b"\n\n"):
			data += self.socket.recv(1024)

		data_decoded = data.decode("utf-8")

		status, payload = data_decoded.split("\n", 1)
		payload = payload.strip()

		if status == "error":
			raise ClientError(payload)

		return payload

	def put(self, key, value, timestamp):
		timestamp = timestamp or str(int(time.time()))
		self.socket.sendall(f"put {key} {value} {timestamp}\n".encode("utf-8"))
		resp = self._read()

	def get(self, key):
		self.socket.sendall(f"get {key}\n".encode("utf-8"))
		payload = self._read()

		data = {}
		if payload == "":
			return data

		for row in payload.split("\n"):
			key, value, timestamp = row.split()
			if key not in data:
				data[key] = []
			data[key].append( (int(timestamp), float(value)) )

		return data
