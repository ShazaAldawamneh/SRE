import json_passing
from random import randint
def setup_bus(num_buses):
    outDict = {}
    for i in range(num_buses):
        temp = {}
        temp["charge"] = 100
        temp["endOfJourney"] = False
        temp["status"] = "parked"
        temp["route_id"] = None
        outDict[i+1] = temp
    json_passing.export_bus(outDict)


def setup_radom_routes(num_routes):
    outDict = {}
    for i in range(num_routes):
        temp = {}
        temp["A_to_B"] = randint(5,20)
        temp["B_to_A"] = randint(5,20)
        temp["A_to_Depot"] = randint(0,15)
        temp["B_to_Depot"] = randint(0,15)
        outDict[i+1] = temp
    json_passing.export_routes(outDict)
