class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def set_data(self,data):
        self.data = data
    def get_data(self):
        return self.data
    
    def set_next(self,next):
        self.next = next
    def get_next(self):
        return self.next
    def has_next(self):
        return self.next != None
    
    def set_prev(self,prev):
        self.prev = prev
    def get_prev(self):
        return self.prev
    def has_prev(self):
        return self.prev != None
    
    def __str__(self):
        return "Mode[Data-%s]" % (self.data,)
    

class DoublyLinkedList:
    def __init__(self): 
        self.head = None
        self.tail = None
        
    def insert(self,data):
        if(self.head == None):
            self.head = Node(data)
            self.tail = self.head
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            current.next = Node(data,None,current)
            self.tail = current.next

    def delete(self,data):
        current = self.head #inisialisasi
        if current.data == data:
            self.head = current.next
            self.head.prev = None
            return True
        if current == None:
            return False
        if self.tail == data:           
            self.tail = self.tail.prev
            self.tail.next = None
            return True
        while current != None:
            if current.data == data:
                current.prev.next = current.next
                current.next.prev = current.prev
                return True
            current = current.next
        return False
    
    def insertAtBegining(self,data):
        newNode = Node(data, None, None)
        if(self.head == None):
            self.head = self.tail = newNode
        else:
            newNode.set_prev(None)
            newNode.set_next(self.head)
            self.head.set_prev(newNode)
            self.head = newNode

    def getNode(self,index):
        currentNode = self.head
        if currentNode == None:
            return None
        i = 0
        while i < index and currentNode.get_next() is not None:
            currentNode = currentNode.get_next()
            if currentNode == None:
                break
            i += 1
        return currentNode
        
    def insertAtGivenPosition(self,index,data):
        newNode = Node(data)
        if self.head == None or index == 0:
            self.insertAtBegining(data)
        elif index < 0:
            temp = self.getNode(index)
            if temp == None or temp.get_next() == None:
                self.insert(data)
            else:
                newNode.set_next(temp.get_next())
                newNode.set_prev(temp)
                temp.get_next().set_prev(newNode)
                temp.set_next(newNode)
                return True
            def find(self,data):
                current = self.head
                while current != None:
                    if current.data == data:
                        return True
                    current = current.next
                return False
            
            def fwd_print(self):
                current = self.head
                if current == None:
                    print("No Elements")
                    return False
                while(current != None):
                    print(current.data)
                    current = current.next
                return True
            
            def rev_print(self):
                current = self.tail
                if (self.tail == None):
                    print("No Elements")
                    return False
                while (current != None):
                    print(current.data)
                    current = current.prev
                return True
            
from doubly import *

dll = DoublyLinkedList()
dll.insert("alice")
print(dll.getNode(0).get_data())
# 'alice'

dll.insert("bob")
dll.insert("charlie")
print(dll.getNode(1).get_data())
# 'bob'
print(dll.getNode(2).get_data())
# 'charlie'

dll.insertAtGivenPosition(1,"donna")
print(dll.getNode(0).get_data())
# 'alice'
print(dll.getNode(1).get_data())
# 'bob'
print(dll.getNode(2).get_data())
# 'donna'
print(dll.getNode(3).get_data())
# 'charlie'
print(dll.delete("donna"))
# True


# jika, ---------------------
dll.insertAtBegining("donna")
print(dll.getNode(0).get_data())
# 'donna'
print(dll.getNode(1).get_data())
# 'bob'
print(dll.getNode(2).get_data())
# 'donna'
print(dll.getNode(3).get_data())
# 'charlie'
