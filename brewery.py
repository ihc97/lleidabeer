# Comments must be kept
import random
import pprint

class Element(object):
    """Element"""
    def __init__(self):
        super(Element, self).__init__()


class Sensor(Element):
    """Sensor"""
    def __init__(self, name="GenericSensor", **kwargs):
        super(Sensor, self).__init__()
        self.calibration = 1.0
        self.name = name
        print("*Creating")
        pprint.pprint(kwargs)

    def get_value(self):
        self.update_value()
        return self.value * self.calibration

    def set_calibration(self, calibration):
        self.calibration = calibration

    def has_alarm(self):
        return False

class FlowSensor(Sensor):
    """FlowSensor"""
    def __init__(self, name="FlowSensor"):
        super(FlowSensor, self).__init__(name)
        self.value = 0

    def update_value(self):
        self.value += 1
        if self.value > 1000:
            self.value = 0

class TemperatureSensor(Sensor):
    """TemperatureSensor"""
    def __init__(self, name="TemperatureSensor", **kwargs):
        super(TemperatureSensor, self).__init__(name, **kwargs)
        self.value = 15.0

    def update_value(self):
        self.value = self.value + random.uniform(-1.0, 1.0)


class CO2Sensor(Sensor):
    """CO2Sensor"""
    def __init__(self, name="CO2Sensor"):
        super(CO2Sensor, self).__init__(name)

    def update_value(self):
        self.value = random.random()*100.0


class ActiveElement(Element):
    """ActiveElement"""
    def __init__(self):
        super(ActiveElement, self).__init__()

    def turn_on(self):
        self.activate(True)
        self.state = True

    def turn_off(self):
        self.activate(False)
        self.state = False

    def get_state(self):
        return self.state

class Heater(ActiveElement):
    """Heater"""
    def __init__(self):
        super(Heater, self).__init__()
        self.state = False

    def activate(self, new_state):
        if new_state:
            print("*")
        else:
            print("-")

class Mixer(ActiveElement):
    """Mixer"""
    def __init__(self):
        super(Mixer, self).__init__()
        self.state = False

    def activate(self, new_state):
        if new_state:
            print("X")
        else:
            print(" ")

class Valve(ActiveElement):
    """Valve"""
    def __init__(self):
        super(Valve, self).__init__()
        self.state = False

    def activate(self, new_state):
        if new_state:
            print("O")
        else:
            print(".")






if __name__ == "__main__":
    t = TemperatureSensor()
    print(t.get_value())

    f = FlowSensor()
    f.set_calibration(2.0)
    print(f.get_value())

    v = Valve()
    v.turn_on()
    v.turn_off()
    v.turn_on()

    h = Heater()
    m = Mixer()
