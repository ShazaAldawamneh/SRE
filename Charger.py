class Charger:
    def __init__(self):
        self.bus = None
        self.charge_time = None

    def get_bus(self):
        return self.bus

    def set_bus(self, bus):
        self.bus = bus

    def get_charge_time(self):
        return self.charge_time

    def set_charge_time(self, charge_time):
        self.charge_time = charge_time

    def reduce_charge_time(self):
        self.charge_time += 1
