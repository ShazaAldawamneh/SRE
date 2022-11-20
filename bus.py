class Bus:
    def __init__(self, bus_id):
        self.id = bus_id
        self.charge = 100
        self.status = "parked"
        self.routeID = None
        self.endOfJourney = False

    def get_bus_id(self):
        return self.id

    def set_charge(self, new_charge):
        self.charge = new_charge

    def get_charge(self) -> int:
        return self.charge

    def set_status(self, new_status):
        self.status = new_status

    def get_status(self) -> str:
        return self.status

    def set_route_id(self, new_route):
        self.routeID = new_route

    def get_route_id(self):
        return self.routeID

    def get_end_of_journey(self):
        return self.endOfJourney

    def end_of_journey_false(self):
        self.endOfJourney = False

    def end_of_journey_true(self):
        self.endOfJourney = True

    def __str__(self):
        return str(self.id) + str(self.charge) + str(self.status) + str(self.routeID) + str(self.endOfJourney)
