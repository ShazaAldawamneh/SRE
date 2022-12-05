from Controller import Controller
from random import randint

def loop(controller, count):
    """ Method for looping through each bus and checking if it has reached the end of its journey. """
    # end_loop = False
    print(f"************LOOP({count})************")
    if not controller.charge_queue.empty():
        print(f"\t{controller.charge_queue}")
    for bus in controller.buses:
            # random check, bus has reached the end
        if randint(0, controller.route_amount * 2) == 0:
            controller.check(bus)
        print(bus)
        print(f"*********END OF LOOP({count})*********\n")
    for charger in controller.chargers:  # iterates over charger to fill and then remove buses from them
        controller.charger_dequeue(charger)

def Sim_Click(controller,MAX):
    count = 0
    controller.start_of_day()
    while count < MAX:
        loop(controller, count)
        count+=1

controller = Controller(50,10)
Sim_Click(controller,100)