class Sensor:
    # NOTE:
    # Renamed id to sensor_id to stop potential interference with id()
    def __init__(self, sensor_id, is_active, carpark):
        self.id = sensor_id
        self.is_active = is_active
        self.carpark = carpark

    def __str__(self):
        return f"ID: {self.id}, carpark {self.is_active}, {self.carpark}"


class EntrySensor(Sensor):
    pass


class ExitSensor(Sensor):
    pass
