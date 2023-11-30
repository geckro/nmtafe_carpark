class Display:
    # NOTE:
    # Renamed id to display_id to stop potential interference with id()
    def __init__(self, display_id, carpark, message="Welcome to the car park", is_on=True):
        """
        Display constructor
        :param display_id: The unique identifier for the display
        :param carpark: The Carpark object associated with the display
        :param message: The default message displayed on the display
        :param is_on: True/False indicating whether the display is turned on
        """
        self.id = display_id
        self.message = message
        self.is_on = is_on
        self.carpark = carpark

    def __str__(self):
        # Added some list comprehension to this in case is_on is off
        # Don't know exactly what "is on" refers to but i would assume this
        return f"Display {self.id}, {self.message, self.carpark if self.is_on else 'off'}"

    def update(self, data):
        """
        Updates the message displayed on the display.
        :param data: A dict containing data to update the display message.
        """
        for key, value in data.items():
            self.message = value
            print(f"{key}: {value}")
