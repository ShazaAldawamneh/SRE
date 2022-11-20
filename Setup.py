import Parser
from random import randint
from Bus import Bus


def setup_bus(num_buses):
    out_list = []
    for i in range(num_buses):
        out_list.append(Bus(i))
    return out_list


def setup_random_routes(num_routes):
    out_dict = {}
    for i in range(num_routes):
        temp = {"A-B": randint(5, 20), "B-A": randint(5, 20), "A-Depot": randint(0, 15), "B-Depot": randint(0, 15)}
        route_id = i
        out_dict[route_id] = temp
    Parser.export_routes(out_dict)


setup_random_routes(1)
