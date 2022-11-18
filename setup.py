import json_passing
from random import randint
def setup_bus(num_buses):
    outDict = {}
    for i in range(num_buses):
        temp = {}
        temp["charge"] = 100
        temp["lastJourney"] = False
        temp["status"] = "parked"
        temp["routeID"] = None
        

        busID = i
        outDict[busID] = temp
    json_passing.export_bus(outDict)


def setup_radom_routes(num_routes):
    outDict = {}
    for i in range(num_routes):
        temp = {}
        temp["A-B"] = randint(5,20)
        temp["B-A"] = randint(5,20)
        temp["A-Depot"] = randint(0,15)
        temp["B-Depot"] = randint(0,15)
        routeID = i
        outDict[routeID] = temp
    json_passing.export_routes(outDict)

setup_radom_routes(1)
