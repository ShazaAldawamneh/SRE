import Routes
from random import randint
from Bus import Bus


def setup_bus(num_buses) -> list:
    """ Creates a list and adds the bus objects with default values. """
    out_list = []
    for i in range(num_buses):
        out_list.append(Bus(i))
    return out_list


def setup_random_routes(num_routes):
    """ Creates a dictionary for the routes and adds random values. """
    out_dict = {}
    for i in range(num_routes):
        temp = {"A-B": randint(5, 20), "B-A": randint(5, 20), "A-Depot": randint(0, 15), "B-Depot": randint(0, 15)}
        route_id = i
        out_dict[route_id] = temp
    Routes.export_routes(out_dict)


setup_random_routes(1)
