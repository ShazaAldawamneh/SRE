from enum import Enum


class State(Enum):
    PARKED = 1
    QUEUED = 2
    CHARGING = 3
    IN_SERVICE = 4


class Direction(Enum):
    A_TO_B = 1
    B_TO_A = 2
    A_TO_DEPOT = 3
    B_TO_DEPOT = 4
    DEPOT_TO_A = 5
    DEPOT_TO_B = 6


print(Direction.B_TO_DEPOT)
