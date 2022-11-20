import Setup
from Charger import Charger
import Parser
from random import randint


class Sim:
    def __int__(self, count, bus_amount, route_amount):
        self.count = count
        self.bus_amount = bus_amount
        self.route_amount = route_amount
        self.buses = Setup.setup_bus(bus_amount)
        self.routes = Setup.setup_random_routes(route_amount)
        self.charge_queue = []
        self.chargers = []

        for i in range(5):
            self.chargers.append(Charger())

    '''count = 0
    bus_amount = 50  # the amount of buses in the system
    route_amount = 10  # the amount of routes in the system
    buses = Setup.setup_bus(bus_amount)  # creation of buses, stating parked and fully charged
    Setup.setup_random_routes(route_amount)  # creation of routes, random values
    charge_queue = []
    #chargers = []'''

    # passes id of the next bus with status parked
    def get_available_bus(self):
        for bus in self.buses:
            if bus.get_status() == "parked":
                return bus

    # sets the next bus that is parked to a particular route in a particular direction
    def set_next_bus_to_route(self, route_id, direction):
        bus = self.get_available_bus()
        bus.set_route_id(route_id)
        bus.set_status(direction)

    # sets every direction of every route to have a bus
    def start_of_day(self):
        routes = Parser.read_routes()
        for i in routes:
            self.set_next_bus_to_route(i, "A-B")
            self.set_next_bus_to_route(i, "B-A")

    start_of_day()

    def loop(self):
        while True:
            self.count += 1
            print(self.count)
            for bus in self.buses:

                if randint(0, self.route_amount * 2) == 0:  # random check

                    if bus.get_status() == "A-B":  # checks direction

                        current_route = Parser.get_route(bus.get_route_id())  # retrives route information

                        charge = bus.get_charge() - current_route["A-B"]  # new charges
                        bus.set_charge(charge)  # updates charge

                        if bus.get_end_of_journey():  # checks if bus should go back to depot
                            bus.end_of_journey_false()
                            bus.set_status("B-Depot")
                        elif current_route["A-B"] + current_route["B-A"] + current_route[
                            "B-Depot"] < charge:  # checks if bus should start journey
                            bus.end_of_journey_true()  # fix wrong direction
                            bus.set_status("B-A")
                            next_bus = self.get_available_bus()  # gets new bus to replace previous

                            next_bus.set_route_id(bus.get_route_id())
                            next_bus.set_status("depot-A")

                        else:
                            bus.set_status("B-A")
                            # bus.set_status("B-A")
                            # json_passing.update_bus(i, "status", "B-A")  # if neither is true tells bus to continue

                    elif bus.get_status() == "B-A":  # repeat as above but other direction
                        current_route = Parser.get_route(bus.get_route_id())  # retrives route information

                        charge = bus.get_charge() - current_route["B-A"]
                        bus.set_charge(charge)

                        if bus.get_end_of_journey():

                            bus.end_of_journey_false()
                            bus.set_status("A-Depot")

                        elif current_route["B-A"] + current_route["A-B"] + current_route["A-Depot"] < charge:

                            bus.end_of_journey_true()
                            bus.set_status("A-B")

                            next_bus = self.get_available_bus()
                            next_bus.set_route_id(bus.get_route_id())
                            next_bus.set_status("depot-A")

                        else:
                            bus.set_status("A-B")

                    elif bus.get_status() == "depot-A":  # checks if bus has been driving from depot to route, if true tells to begin route
                        bus.set_status("A-B")
                    elif bus.get_status() == "depot-B":  # repeat for other direction
                        bus.get_status("A-B")

                    elif bus.get_status() == "A-Depot" or bus.get_status() == "B-Depot":  # checks if bus has just entered depot
                        bus.set_status("queueing")
                        self.charge_queue.append(bus)  # adds to charging queue

            # control flow graph
            for charger in self.chargers:  # iterates over charger to fill and then remove buses from them
                if charger.get_bus() is not None:

                    charger.reduce_charge_time()
                    if charger.get_charge_time() == 0:
                        outbus = charger.get_bus()
                        outbus.set_status("parked")
                        outbus.set_charge(100)
                        charger.set_bus(None)
                if charger.get_bus() is None and self.charge_queue:
                    in_bus = self.charge_queue.pop()
                    in_bus.set_status("Charging")
                    charger.set_bus(in_bus)
                    charger.set_charge_time(5)


if __name__ == "__main__":
    pass
