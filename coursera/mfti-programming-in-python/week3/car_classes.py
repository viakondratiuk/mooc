import os
import csv


class BaseCar:
	
	def __init__(self, car_type, brand, photo_file_name, carrying):
		self.car_type = car_type
		self.brand = brand
		self.photo_file_name = photo_file_name
		self.carrying = float(carrying)

	def get_photo_file_ext(self):
		_, ext = os.path.splitext(self.photo_file_name)
		return ext

class Car(BaseCar):

	def __init__(self, car_type, brand, photo_file_name, carrying, passenger_seats_count):
		super().__init__(car_type, brand, photo_file_name, carrying)
		self.passenger_seats_count = int(passenger_seats_count)


class Truck(BaseCar):
	
	def __init__(self, car_type, brand, photo_file_name, carrying, body_whl):
		super().__init__(car_type, brand, photo_file_name, carrying)
		body_whl = body_whl.split("x") if body_whl else False 
		self.body_length = float(body_whl[0]) if body_whl else 0
		self.body_width = float(body_whl[1]) if body_whl else 0
		self.body_height = float(body_whl[2]) if body_whl else 0

	def get_body_volume(self):
		return self.body_length * self.body_width * self.body_height


class SpecMachine(BaseCar):

	def __init__(self, car_type, brand, photo_file_name, carrying, extra):
		super().__init__(car_type, brand, photo_file_name, carrying)
		self.extra = extra


def get_car_list(csv_filename):
	car_list = []

	if not os.path.isfile(csv_filename):
		return car_list

	with open(csv_filename) as csv_fd:
		reader = csv.reader(csv_fd, delimiter=';')
		next(reader)  # пропускаем заголовок
		for row in reader:
			if len(row) < 7:
				continue

			car_type, brand, passenger_seats_count, photo_file_name, body_whl, carrying, extra = row
			if not car_type or not brand or not photo_file_name or not carrying:
				continue

			if car_type == "car":
				car_list.append(Car(car_type, brand, photo_file_name, carrying, passenger_seats_count))
			elif car_type == "truck":
				car_list.append(Truck(car_type, brand, photo_file_name, carrying, body_whl))
			elif car_type == "spec_machine":
				car_list.append(SpecMachine(car_type, brand, photo_file_name, carrying, extra))

	return car_list

if __name__ == "__main__":
	for car in get_car_list("cars.csv"):
		print(car.get_photo_file_ext())
