from Bus import Bus


class Queue:
    """ Class to represent the charging queue. """
    def __init__(self):
        """ Initialises two lists. """
        self.queue = []

   

    def enqueue(self, newBus: Bus):

        """ Method for enqueueing a bus. """
        for index, oldBus in enumerate(self.queue):
            if newBus.get_charge() <= oldBus.get_charge():
                self.queue.insert(index,newBus)

                break
        else: #Only is called when if statment never succeeds
            self.queue.append(newBus) 
    def dequeue(self) -> Bus:
        """ Method to dequeue a bus.

        Returns the instance of the dequeued bus.
        """
        if self.queue:
            return self.queue.pop()

    def top(self) -> Bus:
        """ Returns the bus at the top of the queue. """
        return self.queue[-1]

    def empty(self) -> bool:
        """ Returns true if the charge queue is empty. """
        return not self.queue

    def length(self) -> int:
        """ Returns the length of the queue. """
        return len(self.queue)

    def __str__(self):
        """ String method for displaying a queue. """
        if len(self.queue) == 0:
            return f"\tCharge Queue:\n\t>--empty-->\n"
        string_list = [f"Charge Queue: >"]
        for item in self.queue:
            string_list.append('--' + str(item.bus_id))
        string_list.append('-->\n')
        return ''.join(string_list)
