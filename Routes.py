import json


def json_read(location):
    """ Reads in a json file and loads it. """
    infile = open(location, "r")
    x = infile.read()
    infile.close()
    return json.loads(x)


def json_updater(location, id_, key, value):
    """ Updates the json file to suit controller format. """
    infile = open(location, "r+")
    db = json.loads(infile.read())
    infile.close()

    changed_item = db[str(id_)]
    changed_item[key] = value
    outfile = open(location, "w")
    outfile.write(json.dumps(db))
    outfile.close()


def update_routes(route_id, key, value):
    """ Update the routes in the json file. """
    json_updater("routes.json", route_id, key, value)


def read_routes() -> dict:
    """ Method to return the entire dictionary of routes. """
    temp = json_read("routes.json")
    return_dict = {}
    for count, value in enumerate(temp):
        return_dict[count] = temp[value]
    return return_dict


def json_export(location, dict_out):
    """ Exports an entire dictionary to a json file at location. """
    outfile = open(location, "w")
    outfile.write(json.dumps(dict_out))
    outfile.close()


def export_routes(dict_out):
    """ Exports routes to the json file. """
    json_export("routes.json", dict_out)


def get_route(route_id):
    """ Returns a route from the json file. """
    routes = read_routes()
    return routes[route_id]
