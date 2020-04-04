class Lamp:
    def __init__(self):
        self.state = False # Lamp is off by default

    def is_on(self):
        return self.state

    def set_on(self):
        self.state = True

    def set_off(self):
        self.state = False

class ColorLamp(Lamp):
    def __init__(self):
        self.color = 'black'

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

class LampArray(ColorLamp):
    def __init__(self):
        self.lamp_list = []

    def add_lamp(self, lamp):
        self.lamp_list.append(lamp)
        return lamp

    def set_on(self):
        for lamp in self.lamp_list:
            lamp.set_on()

    def set_off(self):
        for lamp in self.lamp_list:
            lamp.set_off()

    def check_on(self):
        for lamp in self.lamp_list:
            if lamp.is_on() != True:
                return False
        return True

    def check_off(self):
        for lamp in self.lamp_list:
            if lamp.is_on() != False:
                return False
        return True
