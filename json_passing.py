import json

def json_export(location, dictOut):
    outfile = open(location,"w")


    outfile.write(json.dumps(dictOut))
    outfile.close

def json_read(location):
    infile = open(location,"r")
    x = infile.read()
    infile.close()
    return json.loads(x)

def json_updater(location,id, key, value):
    infile = open(location,"r+")
    db = json.loads(infile.read())
    infile.close
    changedItem =db[str(id)]
    changedItem[key] = value
    outfile = open(location,"w")
    outfile.write(json.dumps(db))
    outfile.close()


def read_bus():
    temp =  json_read("bus.json")
    returnDict = {}
    for count, value in enumerate(temp):   
        returnDict[count] = temp[value]    
    return returnDict
    

def export_bus(dictOut):
    json_export("bus.json" ,dictOut)

def update_bus(id,key,value):
    json_updater("bus.json",id,key,value)

def get_bus(id):
    buses = read_bus()
    return buses[id]

def read_routes():
    temp =  json_read("routes.json")
    returnDict = {}
    for count, value in enumerate(temp):   
        returnDict[count] = temp[value]
    return returnDict

def export_routes(dictOut):
    json_export("routes.json",dictOut)

def update_routes(id,key,value):
    json_updater("routes.json",id,key,value)

def get_route(id):
    routes = read_routes()
    return routes[id]
