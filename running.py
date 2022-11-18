import setup 
import json_passing
from random import randint
count = 0
bus_amount = 50 #the amount of buses in the system
route_amount = 10 # the amount of routes in the system
setup.setup_bus(bus_amount)#creation of buses, stating parked and fully charged
setup.setup_radom_routes(route_amount)# creation of routes, random values
chargeQueue = []
chargers = [{"busID":None,"chargetime":0},{"busID":None,"chargetime":0},{"busID":None,"chargetime":0},{"busID":None,"chargetime":0},{"busID":None,"chargetime":0}]
#passes id of the next bus with status parked
def getAvaliableBus():
    bueses = json_passing.read_bus()
    for i in bueses:
        if bueses[i]["status"] =="parked":
            return i 

#sets the next bus that is parked to a particulat route in a particular direction
def setNextBusToRoute(routeID,direction):
    busID = getAvaliableBus()
    json_passing.update_bus(busID,"routeID",routeID)
    json_passing.update_bus(busID,"status",direction)

#sets every direction of every route to have a bus
def startOfDay():
    routes = json_passing.read_routes()
    for i in routes:
        setNextBusToRoute(i,"A-B")
        setNextBusToRoute(i,"B-A")

        
print(json_passing.read_bus())
startOfDay()
print(json_passing.read_bus())


while True:
    count +=1
    buses = json_passing.read_bus()
    for i in buses:

        if  randint(0,route_amount*2) == 0:#random check
            
            if buses[i]["status"] == "A-B":#checks direction 
                currentRoute = json_passing.get_route(buses[i]["routeID"])#retrives route information

                charge = buses[i]["charge"] - currentRoute["A-B"]#new charges

                json_passing.update_bus(i,"charge",charge)#updates charge


                if buses[i]["lastJourney"]:#checks if bus should go back to depot
                    json_passing.update_bus(i,"lastJourney",False)
                    json_passing.update_bus(i,"status","B-Depot")
                    print(i,"heading back to depot")
                elif currentRoute["A-B"]+currentRoute["B-Depot"] < charge:#checks if bus should start journey
                    json_passing.update_bus(i,"lastJourney",True)
                    json_passing.update_bus(i,"status","A-B")
                    print(i,"begining last journey")
                    nextBus = getAvaliableBus()#gets new bus to replace previous
                    
                    json_passing.update_bus(nextBus,"routeID",buses[i]["routeID"])
                    json_passing.update_bus(nextBus,"status","depot-A")
                    print(nextBus,"leaving station")
                else:
                    json_passing.update_bus(i,"status","B-A")#if neither is true tells bus to continue
                    print(i,"continuing")
            elif buses[i]["status"] == "B-A":#repeat as above but other direction
                currentRoute = json_passing.get_route(buses[i]["routeID"])#retrives route information

                charge = buses[i]["charge"] - currentRoute["B-A"]

                json_passing.update_bus(i,"charge",charge)
                
                if buses[i]["lastJourney"]:

                    json_passing.update_bus(i,"lastJourney",False)
                    json_passing.update_bus(i,"status","A-Depot")
                    print(i,"heading back to depot")
                    

                elif currentRoute["B-A"]+currentRoute["A-Depot"] < charge:

                    json_passing.update_bus(i,"lastJourney",True)
                    json_passing.update_bus(i,"status","B-A")
                    print(i,"begining last journey")

                    nextBus = getAvaliableBus()
                    json_passing.update_bus(nextBus,"routeID",buses[i]["routeID"])
                    json_passing.update_bus(nextBus,"status","depot-A")
                    print(nextBus,"leaving station")

                else:
                    json_passing.update_bus(i,"status","A-B")  
                    print(i,"continuing")
            
            elif buses[i]["status"] == "depot-A":#checks if bus has been driving from depot to route, if true tells to begin route
                json_passing.update_bus(i,"status","A-B")
                print(i, "begining first journey")
            elif buses[i]["status"] == "depot-B":#repeat for other direction
                json_passing.update_bus(i,"status","A-B")
                print(i, "begining first journey")
            elif buses[i]["status"]== "A-Depot" or buses[i]["status"]=="B-Depot":#checks if bus has just entered depot

                json_passing.update_bus(i,"status","queueing")
                chargeQueue.append(i)#adds to charging queue
                print(i, "entering charging queue")
            
        
    for charger in chargers:#iterates over charger to fill and then remove buses from them
        if charger["busID"] != None:

            charger["chargetime"] += -1
            if charger["chargetime"] == 0:
                print("sending", charger["busID"],"to park")
                json_passing.update_bus(charger["busID"],"status","parked")
                json_passing.update_bus(charger["busID"],"charge",100)
                charger["busID"]= None
        elif charger["busID"] == None and chargeQueue:

            charger["busID"] = chargeQueue.pop()
            json_passing.update_bus(charger["busID"],"status","charging")
            charger["chargetime"]=5
            print(charger["busID"],"begining charge")
