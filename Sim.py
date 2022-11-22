import Setup
from ChargingStation import ChargingStation
import Parser
from random import randint


class Sim:
    """ #TODO documentation. """

    def __init__(self, count, bus_amount, route_amount):
        """ #TODO documentation. """
        self.count = count
        self.bus_amount = bus_amount
        self.route_amount = route_amount
        self.buses = Setup.setup_bus(bus_amount)
        Setup.setup_random_routes(route_amount)
        self.charge_queue = [] # queue class needed
        self.chargers = []

        for i in range(5):
            self.chargers.append(ChargingStation())

    '''count = 0
    bus_amount = 50  # the amount of buses in the system
    route_amount = 10  # the amount of routes in the system
    buses = Setup.setup_bus(bus_amount)  # creation of buses, stating parked and fully charged
    Setup.setup_random_routes(route_amount)  # creation of routes, random values
    charge_queue = []
    #chargers = []'''

    # passes id of the next bus with status parked
    def get_available_bus(self):
        """ #TODO Control flow graph here... and documentation. """
        for bus in self.buses:

            
            if bus.get_status() == "PARKED":  # and battery full?
                return bus
        else:

            return self.charger_drop_early()

    # sets the next bus that is parked to a particular route in a particular direction
    def set_next_bus_to_route(self, route_id, direction):
        """ #TODO documentation. """
        bus = self.get_available_bus() # returning None
        bus.set_route_id(route_id)
        bus.set_status(direction)
        #print(bus)


    # sets every direction of every route to have a bus
    # #TODO needs to be fixed
    def start_of_day(self):
        """ #TODO  Control flow graph here... and documentation. """
        routes = Parser.read_routes()
        for i in routes: # goes through every route and assigns a bus
            self.set_next_bus_to_route(i, "A-B")
            self.set_next_bus_to_route(i, "B-A")

    def charger_Check(self,charger):
        if charger.get_bus() is not None:
            charger.reduce_charge_time()
            if charger.get_charge_time() == 0:
                out_bus = charger.get_bus()
                out_bus.set_status("PARKED")
                out_bus.set_charge(100)
                charger.set_bus(None)
                charger.set_charge_time == None
        if charger.get_bus() is None and self.charge_queue:
            in_bus = self.charge_queue.pop()
            in_bus.set_status("CHARGING")
            charger.set_bus(in_bus)
            charger.set_charge_time(5)

    def charger_drop_early(self):
        
        for charge_time in range(1,6):
            
            for charger in self.chargers:
                print(charge_time)
                print(charger.get_bus())
                print(self.charge_queue)
                
           
                if charger.get_charge_time() ==charge_time:
                    print(charger.get_charge_time())
                    out_bus= charger.get_bus()
                   # print(charge_time)
                
                    out_bus.set_charge(100-(20*charge_time))
                    charger.set_bus(None)
                    charger.set_charge_time(None)
  
                    return out_bus

    def loop(self):
        """ #TODO documentation. """

        while True:
            self.count += 1
            print(self.count)
            for bus in self.buses:
                

                if randint(0, self.route_amount * 2) == 0:  # random check, bus has reached the end4

                    # TODO wrap this in a function
                    '''
                    Logic Breakdown. 
                        1. Check status for "A-B" ** maybe be get_journey_status...
                            a. 
                    '''
                    # def function(status):
                    if bus.get_status() == "A-B":  # checks direction
                        
                        # gets current route (maybe different getter?) then parses the json file **
                        current_route = Parser.get_route(bus.get_route_id())  # retrieves route information
                        # performs the operation here
                        charge = bus.get_charge() - current_route["A-B"]  # new charges
                        #
                        bus.set_charge(charge)  # updates charge

                        if bus.get_end_of_journey():  # checks if bus should go back to depot
                            bus.set_end_of_journey(False)
                            bus.set_status("B-Depot")

                            # check battery level
                            # check other details
                            # should do more maybe...?


                        # uni test for this logic
                        elif current_route["A-B"] + current_route["B-A"] + current_route[
                            "B-Depot"] < charge:  # checks if bus should start journey
                            bus.set_end_of_journey(True)  # fix wrong direction
                            bus.set_status("B-A")
                            next_bus = self.get_available_bus()  # gets new bus to replace previous

                            next_bus.set_route_id(bus.get_route_id())
                            next_bus.set_status("Depot-A")
                            
                        else:
                            bus.set_status("B-A")

                    elif bus.get_status() == "B-A":  # repeat as above but other direction
                        current_route = Parser.get_route(bus.get_route_id())  # retrieves route information
                        charge = bus.get_charge() - current_route["B-A"]
                        bus.set_charge(charge)

                        if bus.get_end_of_journey():
                            bus.set_end_of_journey(False)
                            bus.set_status("A-Depot")

                        elif current_route["B-A"] + current_route["A-B"] + current_route["A-Depot"] < charge:
                            bus.set_end_of_journey(True)
                            bus.set_status("A-B")
                            next_bus = self.get_available_bus()
                            next_bus.set_route_id(bus.get_route_id())
                            next_bus.set_status("Depot-B")
                        else:
                            bus.set_status("A-B")

                    elif bus.get_status() == "Depot-A":  # checks if bus has been driving from depot to route,
                        # if true tells to begin route
                        bus.set_status("A-B")
                    elif bus.get_status() == "Depot-B":  # repeat for other direction
                        bus.set_status("A-B")

                    elif bus.get_status() == "A-Depot" or bus.get_status() == "B-Depot":  # checks if bus has just
                        # entered depot
                        bus.set_status("QUEUED")
                        self.charge_queue.append(bus)  # adds to charging queue'
                        print(bus)
                    #print(bus)
            # control flow graph
            # TODO CFG
            for charger in self.chargers:  # iterates over charger to fill and then remove buses from them
                self.charger_Check(charger)
                


if __name__ == "__main__":
    x = Sim(1, 50, 10)
    x.start_of_day()
    x.loop()
