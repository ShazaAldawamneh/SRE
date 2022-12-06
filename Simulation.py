from random import randint


class Simulation:
    """A simulation of the bus-charging algorithm."""

    def loop(self):
        """ Method for looping through each bus and checking if it has reached the end of its journey. """
        for bus in self.buses:
            # random check, bus has reached the end
            if randint(0, self.route_amount * 2) == 0:
                self.bus_manager(bus)

        for charger in self.chargers:  # iterates over charger to fill and then remove buses from them
            self.charger_dequeue(charger)

    def sim_on_click(self, max_loops):
        """Starts initialisation of the bus and ends on the given argument (max_loops)."""
        count = 0
        self.start_of_day()
        while count < max_loops:
            Simulation.loop(self)
            count += 1
