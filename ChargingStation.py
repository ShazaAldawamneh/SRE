class ChargingStation:
    """ Represents a Charging Station """
    def __init__(self):
        """ Create a charging station instance.
        Args:
            bus_id -        bus id associated with a charging station.
            charge_time -   battery charge time.
        """
        self.bus_id = None
        self.charge_time = None

    def get_bus_id(self) -> int:
        """ Return a bus id associated with charging station. """
        return self.bus_id

    def set_bus(self, bus_id: int):
        """ Set a bus id to a charging station. """
        self.bus_id = bus_id

    def get_charge_time(self) -> int:
        """ Return the charge time value. """
        return self.charge_time

    def set_charge_time(self, charge_time: int):
        """ Set a charging station charge time. """
        self.charge_time = charge_time

    def reduce_charge_time(self):
        """ Method to reduce charge time by 1"""
        self.charge_time += 1
