from Enums import State, Direction


class Bus:
    """ A Bus object. """

    def __init__(self, bus_id):
        """ Create a bus instance.

        Args:
            bus_id -    unique id for each bus
            charge -    battery level (min:0, max:100)
            status -    default state of a bus
            route_id -  unique route id associated with a bus
        """
        self.bus_id = bus_id
        self.charge = 100
        self.status = State.PARKED
        self.route_id = None
        self.end_of_journey = False
        self.states = [State.PARKED, State.QUEUED, State.CHARGING, State.IN_SERVICE]

    def get_bus_id(self) -> int:
        """ Returns bus id. """
        return self.bus_id

    def get_charge(self) -> int:
        """ Return bus charge level. """
        return self.charge

    def get_status(self) -> State:
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
        # if new_charge >= 0 or new_charge <= 100:
        self.charge = new_charge
        # else:
            # raise ValueError("Wrong Value")


    def set_status(self, new_status: State) -> None:
        """ Set bus status. """
        if new_status in self.states:
            self.status = new_status
        else:
            raise ValueError("Wrong State")
    def set_route_id(self, new_route: int) -> None:
        """ Set route id associated with a Bus object. """
        self.route_id = new_route

    def set_end_of_journey_false(self, end_flag: bool) -> None:
        """ Set end of journey flag. """
        self.end_of_journey = end_flag

    def __str__(self):
        """ String representation of a Bus object"""
        a = f"\nBus ID:\t\t{str(self.bus_id)}\nCharge(%):\t{str(self.charge)}"
        b = f"\nStatus:\t\t{str(self.status)}\nRoute ID:\t{str(self.route_id)}\n"
        return a + b


if __name__ == "__main__":
    test = Bus(1)
    test2 = Bus(2)
    # test2.set_status(3)
    print(test2)
    test2.set_status(State.IN_SERVICE)
    test2.set_charge("str")
    # test2.set_status(2)
    print(test2)
    # print(test)
