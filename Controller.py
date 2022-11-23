import Setup
from ChargingStation import ChargingStation
import Routes
from random import randint
from Queue import Queue


class Controller:
    """ Controller class """

    def __init__(self, count, bus_amount, route_amount):
        """ Controller Constructor. """
        self.count = count
        self.bus_amount = bus_amount
        self.route_amount = route_amount
        self.buses = Setup.setup_bus(bus_amount)
        Setup.setup_random_routes(route_amount)
        self.charge_queue = Queue()  # queue class needed
        self.chargers = []

        for i in range(5):
            self.chargers.append(ChargingStation())

    def get_available_bus(self):
        """ Method to return the id of the next available bus. """
        flag = True
        for bus in self.buses:
            if bus.get_status() == "PARKED":
                flag = False
                return bus
        if flag:
            return self.charger_drop_early()

    def set_next_bus_to_route(self, route_id, direction):
        """ Set the next available bus to a route. """
        bus = self.get_available_bus()
        bus.set_route_id(route_id)
        bus.set_status(direction)

    def start_of_day(self):
        """ Assigns a bus to a route. """
        routes = Routes.read_routes()
        for i in routes:  # goes through every route and assigns a bus
            self.set_next_bus_to_route(i, "A-B")
            self.set_next_bus_to_route(i, "B-A")

    def charger_dequeue(self, charger):
        """ Method to dequeue a bus from a charging station. """
        if charger.get_bus() is not None:
            charger.reduce_charge_time()
            if charger.get_charge_time() == 0:
                out_bus = charger.get_bus()
                out_bus.set_status("PARKED")
                out_bus.set_charge(100)
                charger.set_bus(None)
                charger.set_charge_time == None
        if charger.get_bus() is None and not self.charge_queue.empty():
            in_bus = self.charge_queue.dequeue()
            print(self.charge_queue)
            in_bus.set_status("CHARGING")
            charger.set_bus(in_bus)
            charger.set_charge_time(5)

    def charger_drop_early(self):
        """ Method that returns bus with the highest charge. """
        for charge_time in range(1, 6):
            for charger in self.chargers:
                if charger.get_charge_time() == charge_time:
                    print(charger.get_charge_time())
                    out_bus = charger.get_bus()
                    out_bus.set_charge(100 - (20 * charge_time))
                    charger.set_bus(None)
                    charger.set_charge_time(None)
                    return out_bus

    def loop(self):
        """ Method for looping through each bus and checking if it has reached the end of its journey. """
        while True:
            self.count += 1
            print(f"************LOOP({self.count})************")
            # print(f"************Loop:\t\t{self.count}*************\n\tLoop:\t\t{self.count}\n************END-OF-LOOP*************\n")
            if not self.charge_queue.empty():
                print(f"\t{self.charge_queue}")
            for bus in self.buses:
                if randint(0, self.route_amount * 2) == 0:  # random check, bus has reached the end
                    if bus.get_status() == "A-B":  # checks direction
                        current_route = Routes.get_route(bus.get_route_id())  # retrieves route information
                        # performs the operation here
                        bus.subtract_charge(current_route["A-B"])
                        charge = bus.get_charge()
                        if bus.get_end_of_journey():  # checks if bus should go back to depot
                            bus.set_end_of_journey(False)
                            bus.set_status("B-Depot")
                        elif current_route["A-B"] + current_route["B-A"] + \
                                current_route["B-Depot"] > charge:  # checks if bus should start journey
                            bus.set_end_of_journey(True)
                            bus.set_status("B-A")
                            next_bus = self.get_available_bus()  # gets new bus to replace previous
                            if next_bus is None:
                                raise Exception("No buses available")
                            next_bus.set_route_id(bus.get_route_id())
                            next_bus.set_status("Depot-A")
                        else:
                            bus.set_status("B-A")
                    elif bus.get_status() == "B-A":  # repeat as above but other direction
                        current_route = Routes.get_route(bus.get_route_id())  # retrieves route information
                        charge = bus.get_charge() - current_route["B-A"]
                        bus.set_charge(charge)
                        if bus.get_end_of_journey():
                            bus.set_end_of_journey(False)
                            bus.set_status("A-Depot")
                        elif current_route["B-A"] + current_route["A-B"] + current_route["A-Depot"] > charge:
                            bus.set_end_of_journey(True)
                            bus.set_status("A-B")
                            next_bus = self.get_available_bus()
                            next_bus.set_route_id(bus.get_route_id())
                            next_bus.set_status("Depot-B")
                        else:
                            bus.set_status("A-B")
                    elif bus.get_status() == "Depot-A":  # checks if bus has been driving from depot to route
                        bus.set_status("A-B")
                    elif bus.get_status() == "Depot-B":  # repeat for other direction
                        bus.set_status("A-B")
                    elif bus.get_status() == "A-Depot" or bus.get_status() == "B-Depot":  # checks if bus has just
                        # entered depot
                        bus.set_status("QUEUED")
                        self.charge_queue.enqueue(bus)  # adds to charging queue'
                        bus.set_route_id(None)
                        print(self.charge_queue)
                    # print(bus)
                print(bus)
            print(f"*********END OF LOOP({self.count})*********\n")
            for charger in self.chargers:  # iterates over charger to fill and then remove buses from them
                self.charger_dequeue(charger)


if __name__ == "__main__":
    x = Controller(1, 50, 10)
    x.start_of_day()
    x.loop()
