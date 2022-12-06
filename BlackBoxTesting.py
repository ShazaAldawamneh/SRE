import unittest
from Simulation import Simulation
from Controller import Controller

class BlackBoxTest(unittest.TestCase):
    def test_simulation_valid(self):
        """ Tests the simulation with valid inputs. Even amount of buses to the number of routes"""
        controller = Controller(50, 10)
        Simulation.sim_on_click(controller, 100)


    def test_simulation_valid_part_two(self):
        """ Tests the simulation with valid inputs. """
        controller = Controller(20, 10)
        Simulation.sim_on_click(controller, 10)


    def test_simulation_valid_part_three(self):
        """ Tests the simulation with valid inputs. """
        controller = Controller(50, 10)
        Simulation.sim_on_click(controller, 10000)

    def test_simulation_invalid_part_one(self):
        """ Tests the simulation with invalid inputs where
            there are not enough of buses per route.
            Note:
                There are two buses allocated per route.
                The test is meant to fail."""
        controller = Controller(10, 10)
        Simulation.sim_on_click(controller, 10)


    def test_simulation_invalid_part_two(self):
        """ Tests the simulation with invalid inputs where
            there are not enough of buses per route.
            Note:
                There are two buses allocated per route.
                The test is meant to fail."""
        controller = Controller(30, 15)
        Simulation.sim_on_click(controller, 75)

if __name__ == '__main__':
    unittest.main()
