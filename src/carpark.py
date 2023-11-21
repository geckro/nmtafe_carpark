from display import Display
from sensor import Sensor


class Carpark:
    def __init__(self, location=None, capacity=0, current_vehicle_count=0, sensors=0, displays=0):
        self.location = location
        self.capacity = capacity
        self.current_vehicle_count = current_vehicle_count
        self.sensors = sensors
        self.displays = displays

    def __str__(self):
        return f"Carpark at {self.location}, with {self.capacity} available bays"

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a sensor or display")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)