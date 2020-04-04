import unittest
from models import LampArray
from models import ColorLamp

class TestColorLamp(unittest.TestCase):
    def setUp(self):
        self.lamp = ColorLamp()

    def test_set_color(self):
        self.lamp.set_color('Red')
        self.assertEqual(self.lamp.get_color(), 'Red')

class TestLampArray(unittest.TestCase):
    def setUp(self):
        self.lamp = LampArray()
    
    def test_list_on(self):
        self.lamp.add_lamp()
        self.lamp.add_lamp()
        self.lamp.set_on()
        self.assertTrue(self.lamp.check_on())

    def test_list_off(self):
        self.lamp.add_lamp()
        self.lamp.add_lamp()
        self.lamp.set_off()
        self.assertTrue(self.lamp.check_off())




if __name__ == "__main__":
    unittest.main()