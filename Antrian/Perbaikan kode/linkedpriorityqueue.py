from node import Node

class LinkedPriorityQueue(Node):
    def __init__(self):
        self._front = None  
        self._size = 0      

    def isEmpty(self):
        return self._front is None

    def enqueue(self, item):
        new_node = Node(item)
        self._size += 1

        if self._front is None:
            self._front = new_node
            return

        if item < self._front.item:  
            new_node.next = self._front
            self._front = new_node
            return

        current = self._front
        while current.next is not None and current.next.item <= item:  
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def dequeue(self):
        if self.isEmpty():
            return None
        item = self._front.item
        self._front = self._front.next
        self._size -= 1
        return item

    def __len__(self):
        return self._size