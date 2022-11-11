import setup 
import json_passing

setup.setup_bus(20)
setup.setup_random_routes(5)


''' function to get next available bus that's 'Parked' and returns its id'''
def getAvaliableBus():
    bueses = json_passing.read_bus()
    for i in bueses:
        if bueses[i]["status"] =="parked":
            return i

''' Set the next bus to a route given. A to B, or B to A'''
def setNextBusToRoute(routeID,direction):
    busID = getAvaliableBus()
    json_passing.update_bus(busID,"routeID",routeID)
    json_passing.update_bus(busID,"status",direction)



''' Sends 2 bus per route at the beginning...'''
def start():
    routes = json_passing.read_routes()
    for i in routes:
        setNextBusToRoute(i,"A-B")
        setNextBusToRoute(i,"B-A")
        
        

print(json_passing.read_bus())
start()
print(json_passing.read_bus())