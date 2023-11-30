from display import Display
from sensor import Sensor


class Carpark:
    def __init__(self, location=None, capacity=0, current_vehicle_count=0, sensors=0, displays=0):
        """
        Carpark class that represents a carpark place.
        :param location: The location of the parking space in the carpark
        :param capacity: How many parking spaces there are in the carpark
        :param current_vehicle_count: How many vehicles are in the carpark
        :param sensors: Sensors obj
        :param displays: Displays obj
        """
        self.location = location
        self.capacity = capacity
        self.current_vehicle_count = current_vehicle_count
        self.sensors = sensors or []
        self.displays = displays or []

        self.plates = []

    def __str__(self):
        """
        Return string of available carpark bay
        :return: A string indicating the car park's location and available bays
        """
        return f"Carpark at {self.location}, with {self.capacity} available bays"

    def register(self, component):
        """
        Registers a Sensor or Display object to the car park.
        :param component: A Sensor or Display object to be registered
        """
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a sensor or display")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        """
        Adds a vehicle to the car park.
        :param plate: The license plate of the vehicle to be added
        """
        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate):
        """
        Removes a vehicle from the car park
        :param plate: The license plate of the vehicle to be removed
        """
        self.plates.remove(plate)
        self.update_displays()

    @property
    def available_bays(self):
        """
        Calculates the number of available parking bays in the car park
        :return: The number of available parking bays
        """
        if len(self.plates) >= self.capacity:
            return 0
        else:
            return self.capacity - len(self.plates)

    def update_displays(self):
        """
        Updates the Display objects in the car park with information about available bays and static int temperature
        """
        data = {"available_bays": self.available_bays, "temperature": 25}
        for display in self.displays:
            display.update(data)
