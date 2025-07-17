from priorityqueue import PriorityQueue

class ServiceType(object):
    def __init__(self, level):
        self._level = level 

    def __eq__(self, other):
        return self._level == other._level

    def __lt__(self, other):
        return self._level < other._level

    def __le__(self, other):
        return self._level <= other._level

    def __str__(self):
        if self._level == 1: return "Pengaduan Kritis"
        elif self._level == 2: return "Transaksi Besar"
        else: return "Layanan Umum"

class Customer(object):
    def __init__(self, name, service_type):
        self._name = name
        self._service_type = service_type

    def __eq__(self, other):
        return self._service_type == other._service_type

    def __lt__(self, other):
        return self._service_type < other._service_type

    def __le__(self, other):
        return self._service_type <= other._service_type

    def __str__(self):
        return self._name + " / " + str(self._service_type)

class BankModel(object):
    def __init__(self):
        self._queue = PriorityQueue()

    def isEmpty(self):
        return self._queue.isEmpty()

    def addCustomer(self, customer):
        self._queue.enqueue(customer)

    def serveNext(self):
        return self._queue.dequeue()
