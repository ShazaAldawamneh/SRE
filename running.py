import setup 
import json_passing

setup.setup_bus(20)
setup.setup_radom_routes(5)

def getAvaliableBus():
    bueses = json_passing.read_bus()
    for i in bueses:
        if bueses[i]["status"] =="parked":
            return i 
def setNextBusToRoute(routeID,direction):
    busID = getAvaliableBus()
    json_passing.update_bus(busID,"routeID",routeID)
    json_passing.update_bus(busID,"status",direction)


def start():
    routes = json_passing.read_routes()
    for i in routes:
        setNextBusToRoute(i,"A-B")
        setNextBusToRoute(i,"B-A")
        
        

print(json_passing.read_bus())
start()
print(json_passing.read_bus())