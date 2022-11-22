from Bus import Bus


class Queue:
    """ Class to represent the charging queue. """
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def enqueue(self, bus: Bus):
        """ Method for enqueueing a bus. """
        while self.queue1:
            self.queue2.append(self.queue1.pop())
        self.queue1.append(bus)

        while self.queue2:
            self.queue1.append(self.queue2.pop())

    def dequeue(self) -> Bus:
        """ Method to dequeue a bus. """
        if self.queue1:
            return self.queue1.pop()

    def top(self) -> Bus:
        """ Returns the bus at the top of the queue. """
        return self.queue1[-1]

    def empty(self) -> bool:
        """ Return true if the charge queue is empty. """
        return not self.queue1

    def length(self) -> int:
        """ Return the length of the queue. """
        return len(self.queue1)

    def __str__(self):
        """ String method for displaying a queue. """
        if len(self.queue1) == 0:
            return f"Charge Queue: <-empty-<\n"
        string_list = [f"Charge Queue: <"]
        for item in self.queue1:
            string_list.append('-' + str(item.bus_id))
        string_list.append('-<\n')
        return ''.join(string_list)
