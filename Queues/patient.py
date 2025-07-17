from queue import Queue
from condition import Condition

class Patient(object):
    def __init__(self, name, condition):
        self.name = name
        self.condition = condition
    
    def __ge__ (self,other):
        return self.condition >= other.condition
    
    def __str__(self):
        return self.name + " / " + str(self.condition)