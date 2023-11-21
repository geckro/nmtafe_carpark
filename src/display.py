class Display:
    # NOTE:
    # Renamed id to display_id to stop potential interference with id()
    def __init__(self, display_id, carpark, message="", is_on=False):
        self.id = display_id
        self.message = message
        self.is_on = is_on
        self.carpark = carpark

    def __str__(self):
        # Added some list comprehension to this in case is_on is off
        # Don't know exactly what "is on" refers to but i would assume this
        return f"Display {self.id}, {self.message, self.carpark if self.is_on else 'off'}"
