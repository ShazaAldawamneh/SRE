import json
# parser class??

'''exports a dict to json with a given filename'''


def json_export(location, dictOut):
    outfile = open(location, "w")

    outfile.write(json.dumps(dictOut))
    outfile.close


''' Reads the entire dictionary from json'''
def json_read(location):
    infile = open(location, "r")
    x = infile.read()
    infile.close()
    # loads json into dict
    return json.loads(x)


''' Updates a single key, value pair. id is the key of the outer dictionary, 
    key is the key, value pair in the nested dict'''


def json_updater(location, id, key, value):
    infile = open(location, "r+")
    # db is a python dict
    db = json.loads(infile.read())
    infile.close
    # assigns the changed
    changedItem = db[str(id)]
    # update the value of the changed item
    changedItem[key] = value
    outfile = open(location, "w")
    # dumps the dict into json
    outfile.write(json.dumps(db))
    outfile.close()


''' Helper function to simplify the ... changes id back to int.'''
def read_bus():
    temp = json_read("bus.json")
    returnDict = {}
    for count, value in enumerate(temp):
        returnDict[count] = temp[value]
    return returnDict

''' Helper '''
def export_bus(dictOut):
    json_export("bus.json", dictOut)


''' Helper function for updating buses'''
def update_bus(id, key, value):
    json_updater("bus.json", id, key, value)

''' Getter for particular buses as dict'''
def get_bus(id):
    buses = read_bus()
    return buses[str(id)]

''' Helper funciton for changeing route_id back to int'''
def read_routes():
    temp = json_read("routes.json")
    returnDict = {}
    for count, value in enumerate(temp):
        returnDict[count] = temp[value]
    return returnDict

''' overwrites entire routes.json file'''
def export_routes(dictOut):
    json_export("routes.json", dictOut)

''' updates entire routes.json'''
def update_routes(id, key, value):
    json_updater("routes.json", id, key, value)

''' return single route as a dict'''
def get_route(id):
    routes = read_routes()
    return routes[str(id)]
