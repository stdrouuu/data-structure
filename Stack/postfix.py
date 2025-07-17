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

#ditambahkan 2 baris ini saja dari file stack.py------------       
    def __str__(self):          
        return str(self.data) 
#-----------------------------------------------------------



from postfix import Stack

def mathOpr(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2    
    elif op == "-":
        return op1 - op2   
    
def postFixEval(postfixExp):
    tokenlst = postfixExp.split()
    lenLst = len(tokenlst)
    oprdStack = Stack(lenLst)
    for token in tokenlst:
        if token in '0123456789':
            oprdStack.push(int(token))
        else:
            oprd2 = oprdStack.pop()
            oprd1 = oprdStack.pop()
            result = mathOpr(token, oprd1, oprd2)
            oprdStack.push(result)
    return oprdStack.pop()
    

from postfix import *
result = postFixEval('1 2 3 * + 5 -')  
print(result) 
