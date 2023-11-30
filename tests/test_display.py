import unittest
from display import Display
from carpark import Carpark


class TestDisplay(unittest.TestCase):
    def setUp(self):
        carpark_instance = Carpark()
        self.display = Display(1, carpark_instance)

    def test_display_initialized_with_all_attributes(self):
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.id, 1)
        self.assertEqual(self.display.message, "Welcome to the car park")
        self.assertEqual(self.display.is_on, True)
        self.assertIsInstance(self.display.carpark, Carpark)

    def test_update(self):
        self.display.update({"message": "Goodbye"})
        self.assertEqual(self.display.message, "Goodbye")


if __name__ == "__main__":
    unittest.main()
