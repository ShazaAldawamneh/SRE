import json_passing
from random import randint

''' Sets the number of buses to 'Parked' 
id's start at 0'''
def setup_bus(num_buses):
    outDict = {}
    for i in range(num_buses):
        temp = {}
        temp["charge"] = 100
        temp["endOfJourney"] = False
        temp["status"] = "parked"
        temp["routeID"] = None
        busID = i
        outDict[busID] = temp
    json_passing.export_bus(outDict)

''' sets up random values for testing '''
def setup_random_routes(num_routes):
    outDict = {}
    for i in range(num_routes):
        temp = {}
        temp["A_to_B"] = randint(5,20)
        temp["B_to_A"] = randint(5,20)
        temp["A_to_Depot"] = randint(0,15)
        temp["B_to_Depot"] = randint(0,15)
        routeID = i
        outDict[routeID] = temp
    json_passing.export_routes(outDict)

