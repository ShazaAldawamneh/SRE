class Bus:
    """ A Bus object. """

    def __init__(self, bus_id):
        """ Create a bus instance.

        Attributes:
            bus_id-    unique id for each bus
            charge -    battery level (min:0, max:100)
            status -    default state of a bus
            route_id -  unique route id associated with a bus
        """
        self.bus_id = bus_id
        self.charge = 100
        self.status = "PARKED"
        self.route_id = None
        self.end_of_journey = False
        self.states = ["PARKED", "QUEUED", "CHARGING", "A-B","B-A","A-Depot","B-Depot","Depot-A","Depot-B"]

    def get_bus_id(self) -> int:
        """ Returns bus id. """
        return self.bus_id

    def get_charge(self) -> int:
        """ Return bus charge level. """
        return self.charge

    def get_status(self) -> str:
        """ Return bus status. """
        return self.status

    def get_route_id(self) -> int:
        """ Return route id associated with a Bus object. """
        return self.route_id

    def get_end_of_journey(self) -> bool:
        """ Return true if a bus has reached the end of a journey. """
        return self.end_of_journey

    def set_charge(self, new_charge: int) -> None:
        """ Set charge level. """
        self.charge = new_charge

    def set_status(self, new_status: str) -> None:
        """ Set bus status. """
        if new_status in self.states:
            self.status = new_status

    def set_route_id(self, new_route: int) -> None:
        """ Set route id associated with a Bus object. """
        self.route_id = new_route

    def set_end_of_journey(self, end_flag: bool) -> None:
        """ Set end of journey flag. """
        self.end_of_journey = end_flag

    def subtract_charge(self, distance: int):
        self.charge -= distance

    def __str__(self):
        """ String representation of a Bus object"""
        a = f"\tBus ID:\t\t{str(self.bus_id)}\n\tCharge(%):\t{str(self.charge)}"
        b = f"\n\tStatus:\t\t{str(self.status)}\n\tRoute ID:\t{str(self.route_id)}\n"
        return a + b


if __name__ == "__main__":
    test = Bus(1)
    test2 = Bus(2)
    test2.set_status(3)
    test2.set_status("Charging")

    print(test2)
    # print(test)
