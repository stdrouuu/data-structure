class Queue:
    def __init__(self):
        self.array = []

    def isEmpty(self):
        return len(self.array) == 0
    
    def long(self):
        return len(self.array)
    
    def queFront(self):
        if self.isEmpty():
            return None
        return self.array[0]
    
    def addQue(self,data):
        self.array.append(data)

    def remQue(self):
        if self.isEmpty():
            print("Underflow")
            return None
        data = self.array[0]
        self.array.remove(data)
        return data
    
#from queue import *
#antrian = Queue()
#panjang_antrian = 5
#antrian.addQue(10)
#while panjang_antrian > 0