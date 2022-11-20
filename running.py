import setup 
from charger import Charger
import json_passing
from random import randint
count = 0
bus_amount = 50 #the amount of buses in the system
route_amount = 10 # the amount of routes in the system
buses = setup.setup_bus(bus_amount)#creation of buses, stating parked and fully charged
setup.setup_radom_routes(route_amount)# creation of routes, random values
chargeQueue = []
chargers = []
for i in range(5):
    chargers.append(Charger())
#passes id of the next bus with status parked
def getAvaliableBus():
    for bus in buses:
        if bus.get_status() == "parked":
            return bus

#sets the next bus that is parked to a particulat route in a particular direction
def setNextBusToRoute(routeID,direction):
    bus = getAvaliableBus()
    bus.set_route_id(routeID)
    bus.set_status(direction)

#sets every direction of every route to have a bus
def startOfDay():
    routes = json_passing.read_routes()
    for i in routes:
        setNextBusToRoute(i,"A-B")
        setNextBusToRoute(i,"B-A")

        

startOfDay()



while True:
    count +=1
    print(count)
    for bus in buses:
             
        if  randint(0,route_amount*2) == 0:#random check
            
            if bus.get_status() == "A-B":#checks direction

                
                currentRoute = json_passing.get_route(bus.get_route_id())#retrives route information

                charge = bus.get_charge() - currentRoute["A-B"]#new charges
                bus.set_charge(charge)#updates charge


                if bus.get_end_of_journey():#checks if bus should go back to depot
                    bus.end_of_journey_false()
                    bus.set_status("B-Depot")
                elif currentRoute["A-B"]+currentRoute["B-A"]+currentRoute["B-Depot"] < charge:#checks if bus should start journey
                    bus.end_of_journey_true() # fix wrong direction
                    bus.set_status("B-A")
                    nextBus = getAvaliableBus()#gets new bus to replace previous
                    
                    nextBus.set_route_id(bus.get_route_id())
                    nextBus.set_status("depot-A")

                   
                else:
                    bus.set_status("B-A")
                    json_passing.update_bus(i,"status","B-A")#if neither is true tells bus to continue
                    
            elif bus.get_status() == "B-A":#repeat as above but other direction
                currentRoute = json_passing.get_route(bus.get_route_id())#retrives route information

                charge = bus.get_charge() - currentRoute["B-A"]
                bus.set_charge(charge)
                
                if bus.get_end_of_journey():

                    bus.end_of_journey_false()
                    bus.set_status("A-Depot")

                elif currentRoute["B-A"]+currentRoute["A-B"]+currentRoute["A-Depot"] < charge:
                    
                    bus.end_of_journey_true()
                    bus.set_status("A-B")
                    

                    nextBus = getAvaliableBus()
                    nextBus.set_route_id(bus.get_route_id())
                    nextBus.set_status("depot-A")

                else:
                    bus.set_status("A-B")
            
            elif bus.get_status() == "depot-A":#checks if bus has been driving from depot to route, if true tells to begin route
                bus.set_status("A-B")
            elif bus.get_status() == "depot-B":#repeat for other direction
                bus.get_status("A-B")
        
            elif bus.get_status() == "A-Depot" or bus.get_status() == "B-Depot":#checks if bus has just entered depot
                bus.set_status("queueing")
                chargeQueue.append(bus)#adds to charging queue

              
            
#control flow graph         
    for charger in chargers:#iterates over charger to fill and then remove buses from them
        if charger.getBus() != None:

            charger.reduceChargeTime()
            if charger.getChargeTime() == 0:
                outbus = charger.getBus()
                outbus.set_status("parked")
                outbus.set_charge(100)
                charger.setBus(None)
        if charger.getBus() == None and chargeQueue:
            inbus = chargeQueue.pop()
            inbus.set_status("Charging")
            charger.setBus(inbus)
            charger.setChargeTime(5)

