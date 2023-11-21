import random

from carpark import Carpark
from abc import ABC, abstractmethod


class Sensor(ABC):
    # NOTE:
    # Renamed id to sensor_id to stop potential interference with id()
    def __init__(self, sensor_id, is_active, carpark):
        self.id = sensor_id
        self.is_active = is_active
        self.carpark = carpark

    def __str__(self):
        return f"ID: {self.id}, carpark {self.is_active}, {self.carpark}"

    @abstractmethod
    def update_carpark(self, plate):
        pass

    def _scan_plate(self):
        return 'FAKE-' + format(random.randint(0, 999), "03d")

    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_carpark(plate)


class EntrySensor(Sensor):
    def update_carpark(self, plate):
        self.carpark.add_car(plate)
        print(f"Incoming 🚘 vehicle detected. Plate: {plate}")


class ExitSensor(Sensor):
    def update_carpark(self, plate):
        self.carpark.remove_car(plate)
        print(f"Outgoing 🚗 vehicle detected. Plate: {plate}")

    def _scan_plate(self):
        return random.choice(self.carpark.plates)

