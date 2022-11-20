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
        if bus.getStatus() == "parked":
            return bus

#sets the next bus that is parked to a particulat route in a particular direction
def setNextBusToRoute(routeID,direction):
    bus = getAvaliableBus()
    bus.setRouteID(routeID)
    bus.setStatus(direction)

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
            
            if bus.getStatus() == "A-B":#checks direction 

                
                currentRoute = json_passing.get_route(bus.getRouteID())#retrives route information

                charge = bus.getCharge() - currentRoute["A-B"]#new charges
                bus.setCharge(charge)#updates charge


                if bus.getEndOfJourney():#checks if bus should go back to depot
                    bus.endOfJourneyFalse()
                    bus.setStatus("B-Depot")
                elif currentRoute["A-B"]+currentRoute["B-A"]+currentRoute["B-Depot"] < charge:#checks if bus should start journey
                    bus.endOfJourneyTrue() # fix wrong direction 
                    bus.setStatus("B-A")
                    nextBus = getAvaliableBus()#gets new bus to replace previous
                    
                    nextBus.setRouteID(bus.getRouteID())
                    nextBus.setStatus("depot-A")

                   
                else:
                    bus.setStatus("B-A")
                    json_passing.update_bus(i,"status","B-A")#if neither is true tells bus to continue
                    
            elif bus.getStatus() == "B-A":#repeat as above but other direction
                currentRoute = json_passing.get_route(bus.getRouteID())#retrives route information

                charge = bus.getCharge() - currentRoute["B-A"]
                bus.setCharge(charge)
                
                if bus.getEndOfJourney():

                    bus.endOfJourneyFalse()
                    bus.setStatus("A-Depot")

                elif currentRoute["B-A"]+currentRoute["A-B"]+currentRoute["A-Depot"] < charge:
                    
                    bus.endOfJourneyTrue()
                    bus.setStatus("A-B")
                    

                    nextBus = getAvaliableBus()
                    nextBus.setRouteID(bus.getRouteID())
                    nextBus.setStatus("depot-A")

                else:
                    bus.setStatus("A-B")
            
            elif bus.getStatus() == "depot-A":#checks if bus has been driving from depot to route, if true tells to begin route
                bus.setStatus("A-B")
            elif bus.getStatus() == "depot-B":#repeat for other direction
                bus.getStatus("A-B")
        
            elif bus.getStatus() ==  "A-Depot" or bus.getStatus() == "B-Depot":#checks if bus has just entered depot
                bus.setStatus("queueing")
                chargeQueue.append(bus)#adds to charging queue

              
            
#control flow graph         
    for charger in chargers:#iterates over charger to fill and then remove buses from them
        if charger.getBus() != None:

            charger.reduceChargeTime()
            if charger.getChargeTime() == 0:
                outbus = charger.getBus()
                outbus.setStatus("parked")
                outbus.setCharge(100)
                charger.setBus(None)
        if charger.getBus() == None and chargeQueue:
            inbus = chargeQueue.pop()
            inbus.setStatus("Charging")
            charger.setBus(inbus)
            charger.setChargeTime(5)

