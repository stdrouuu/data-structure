from linkedpriorityqueue import LinkedPriorityQueue

class Condition(object):
    def __init__(self, rank):
        self._rank = rank

    def __eq__(self, other):
        return self._rank == other._rank

    def __lt__(self, other):
        return self._rank < other._rank

    def __le__(self, other):
        return self._rank <= other._rank

    def __str__(self):
        if   self._rank == 1: return "critical"
        elif self._rank == 2: return "serious"
        else:                 return "fair"

class Patient(object):
    def __init__(self, name, condition):
        self._name = name
        self._condition = condition

    def __eq__(self, other):
        return self._condition == other._condition

    def __lt__(self, other):
        return self._condition < other._condition

    def __le__(self, other):
        return self._condition <= other._condition

    def __str__(self):
        return self._name + " / " + str(self._condition)

class ERModel(object):

    def __init__(self):
        self._queue = LinkedPriorityQueue()  

    def isEmpty(self):
        return self._queue.isEmpty()  

    def schedule(self, p):
        self._queue.enqueue(p)  

    def treatNext(self):
        return self._queue.dequeue()  