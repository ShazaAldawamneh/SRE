import unittest
from Bus import Bus
from Controller import Controller

class MyTestCase(unittest.TestCase):
    def test_bus_subtract_charge(self):
        """ Testing subtract_charge() in the Bus class.

         A bus instance has 100 charge upon creation.
         """
        test_bus = Bus(1)
        test_bus.subtract_charge(25)
        self.assertEqual(test_bus.get_charge(), 75)

    def test_controller_drop_early(self):
        """ Testing the drop_early() in the Controller class.


         """
        test_controller = Controller(0, 5, 3)

        for bus in test_controller.buses:
            test_controller.charge_queue.enqueue(bus)

        for charger in test_controller.chargers:
            test_controller.charger_dequeue(charger)

        test_controller.chargers[0].set_charge_time(1)
        test_controller.chargers[1].set_charge_time(1)
        test_controller.chargers[2].set_charge_time(2)

        test_controller.charger_drop_early()

        self.assertIsNone(test_controller.chargers[0].get_bus())
        self.assertIsNotNone(test_controller.chargers[1].get_bus())
        self.assertIsNotNone(test_controller.chargers[2].get_bus())

        test_controller.charger_drop_early()

        self.assertIsNone(test_controller.chargers[1].get_bus())
        self.assertIsNotNone(test_controller.chargers[2].get_bus())

        test_controller.charger_drop_early()

        self.assertIsNone(test_controller.chargers[2].get_bus())






if __name__ == '__main__':
    unittest.main()
