import Parser
from random import randint
from Bus import Bus
from Enums import Direction


def setup_bus(num_buses):
    """ #TODO documentation. """
    out_list = []
    for i in range(num_buses):
        out_list.append(Bus(i))
    return out_list


def setup_random_routes(num_routes):
    """ #TODO documentation. """
    out_dict = {}
    for i in range(num_routes):
        temp = {Direction.A_TO_B: randint(5, 20), Direction.B_TO_A: randint(5, 20), Direction.A_TO_DEPOT: randint(0, 15), Direction.B_TO_DEPOT: randint(0, 15)}
        route_id = i
        out_dict[route_id] = temp
    Parser.export_routes(out_dict)


setup_random_routes(1)
