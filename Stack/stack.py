class Stack:
    def __init__(self, C = 5):
        self.C = C
        self.array = []

    def size(self):
        return len(self.array)
    
    def isEmpty(self):
        return len(self.array) == 0
    
    def isFull(self):
        return len(self.array) == self.C
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.array[self.size()-1]
    
    def pop(self):
        if self.isEmpty():
            print ("Underflow")
            return None
        data = self.array.pop()
        return data
    
    def push(self,data):
        if self.isFull():
            print("Overflow")
            return
        self.array.append(data)


from stack import Stack

import random
sizeStack = 6
st = Stack(sizeStack)
while(sizeStack):
    data = random.randrange(1,100)
    print("Pushing", data)
    st.push(data)
    sizeStack -= 1
print("Stack Size", st.size())
print("Top Stack", st.peek())
print("Popping", st.pop())
print("Top Stack", st.peek())



