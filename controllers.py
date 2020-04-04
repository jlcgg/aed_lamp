from models import Lamp
from models import ColorLamp
from models import LampArray

class LampController:
    def __init__(self):
        self.lamps = []

    def set_on(self, id):
        for lamp in self.lamps:
            if lamp['ID'] == id:
                lamp['lamp'].set_on()

    def set_off(self, id):
        for lamp in self.lamps:
            if lamp['ID'] == id:
                lamp['lamp'].set_off()

    def get_status(self, id):
        for lamp in self.lamps:
            if lamp['ID'] == id:
                return lamp['lamp'].is_on()

    def create_lamp(self, id):
        lamp = Lamp()

        dic = {
            'ID': id,
            'lamp': lamp
        }

        self.lamps.append(dic)

    def create_colorLamp(self, id, color):
        lamp = ColorLamp(color)

        dic = {
            'ID': id,
            'lamp': lamp
        }

        self.lamps.append(dic)

    def create_lampArray(self, id):
        lamp = LampArray()

        dic = {
            'ID': id,
            'lamp': lamp
        }

        self.lamps.append(dic)

    def add_lamp(self, lamp_id, lampArray_id):
        for lamp in self.lamps:
            if lamp['ID'] == lampArray_id:
                for new_lamp in self.lamps:
                    if new_lamp['ID'] == lamp_id:
                        lamp.append(new_lamp)   