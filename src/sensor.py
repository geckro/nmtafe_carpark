import random

from abc import ABC, abstractmethod


class Sensor(ABC):
    """
    Abstract base class for sensors in a car park
    """
    # NOTE:
    # Renamed id to sensor_id to stop potential interference with id()
    def __init__(self, sensor_id, is_active, carpark):
        """
        Sensor constructor

        :param sensor_id: The unique ID for the sensor
        :param is_active: True/False indicating whether the sensor is active
        :param carpark: The Carpark object associated with the sensor
        """
        self.id = sensor_id
        self.is_active = is_active
        self.carpark = carpark

    def __str__(self):
        """
        Returns a string representation of the sensor.

        :return: A string containing the sensor's ID, activity status, and associated car park
        """
        return f"ID: {self.id}, carpark {self.is_active}, {self.carpark}"

    @abstractmethod
    def update_carpark(self, plate):
        """
        Abstract method to update the car park based on sensor detection.
        :param plate: The license plate of the detected vehicle.
        """
        pass

    def _scan_plate(self):
        """
        Generates a fake license plate
        :return: A string representing a fake license plate
        """
        return 'FAKE-' + format(random.randint(0, 999), "03d")

    def detect_vehicle(self):
        """
        Generates a fake license plate and updates the car park
        """
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

