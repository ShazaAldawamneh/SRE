import json


def json_read(location):
    """ Reads in a json file and loads it. """
    infile = open(location, "r")
    x = infile.read()
    infile.close()
    return json.loads(x)


def json_updater(location, id_, key, value):
    """ #TODO documentation. """
    infile = open(location, "r+")
    db = json.loads(infile.read())
    infile.close()

    changed_item = db[str(id_)]
    changed_item[key] = value
    outfile = open(location, "w")
    outfile.write(json.dumps(db))
    outfile.close()


def update_routes(route_id, key, value):
    """ #TODO documentation. """
    json_updater("routes.json", route_id, key, value)


def read_routes():
    """ #TODO documentation. """
    temp = json_read("routes.json")
    return_dict = {}
    for count, value in enumerate(temp):
        return_dict[count] = temp[value]
    return return_dict


def json_export(location, dict_out):
    """ #TODO documentation. """
    outfile = open(location, "w")
    outfile.write(json.dumps(dict_out))
    outfile.close()


def export_routes(dict_out):
    """ #TODO documentation. """
    json_export("routes.json", dict_out)


def get_route(route_id):
    """ #TODO documentation. """
    routes = read_routes()
    return routes[route_id]
