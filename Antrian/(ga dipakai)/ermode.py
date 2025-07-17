# pernah diketik sebagian di patient.py
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
        if self._rank == 1: return "critical"
        elif self._rank == 2: return "serious"
        else: return "fair"
        
class Patient(object):
    def __init__(self, name, condition):
        self.name = name
        self.condition = condition
    
    def __eq__ (self,other):
        return self.condition == other.condition
    
    def __lt__ (self,other):
        return self.condition < other.condition
    
    def __le__ (self,other):
        return self.condition <= other.condition
    
    def __str__(self):
        return self.name + " / " + str(self.condition)
    
class ERModel(object):
    def __init__(self):
        pass

    def isEmpty(self):
        return True
    
    def schedule(self,p):
        pass

    def treatNext(self):
        return None
