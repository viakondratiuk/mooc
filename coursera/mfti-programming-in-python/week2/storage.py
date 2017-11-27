import argparse
import os
import tempfile


parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--val")
args = parser.parse_args()
key = args.key
val = args.val

storage_file = os.path.join(tempfile.gettempdir(), "storage.data")

if val:
	with open(storage_file, "a") as f:
		f.write("{}:{}\n".format(key, val))
else:
	if not os.path.exists(storage_file):
		print("")
	else:
		with open(storage_file, "r") as f:
			if not f:
				print("")
			else:
				output = []
				data = f.readlines()
				for el in data:
					spl = el.split(":")
					if key == spl[0]:
						output.append(spl[1].strip())
				print(", ".join(output))			 
