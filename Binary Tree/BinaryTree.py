class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.last = None
        self.next = next

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
    
    def setLast(self,last):
        self.last = last
    def getLast(self):
        return self.last

class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def set_data(self,data):
        self.data = data

    def get_data(self):
        return self.data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.left = self.left
            self.left = temp

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.right = self.right
            self.right = temp

class Queue(object):
    def __init__(self, data = None):
        self.front = None
        self.rear = None
        self.size = 0

    def enQueue(self,data):
        self.lastNode = self.front
        self.front = Node(data,self.front)
        if self.lastNode:
            self.lastNode.setLast(self.front)
        if self.rear is None:
            self.rear = self.front
        self.size += 1

    def deQueue(self):
        if self.rear is None:
            print ("Empty")
            raise IndexError
        result = self.rear.get_data()
        self.rear = self.rear.last
        self.size -= 1
        return result

    def isEmpty(self):
        return self.size == 0

def insertNodeLO(root, data):
    newNode = BinaryTree(data)
    if root is None:
        root = newNode
        return root

    q = Queue()
    q.enQueue(root)
    node = None
    while not q.isEmpty():
        node = q.deQueue()
        if data == node.get_data():
            return root
        if node.left is not None:
            q.enQueue(node.left)
        else:
            node.left = newNode
            return root
        if node.right is not None:
            q.enQueue(node.right)
        else:
            node.right = newNode
            return root

def preOrder(root,result):
    if not root:
        return
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        result.append(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def inOrder(root,result):
    if not root:
        return
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            result.append(node.data)
            node = node.right
    
def postOrder(root, result): #kiri kanan tengah
    if not root:
        return

    visited = set()
    stack = []
    node = root
    while stack or node: #OR -> salah satu antara stack atau node-> (selama stack atau node berisi)
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if node.right and not node.right in visited:
                stack.append(node)
                node = node.right
            else:
                visited.add(node)
                result.append(node.data)
                node = None

root = BinaryTree(1)
root = insertNodeLO(root, 2)
root = insertNodeLO(root, 3)
root = insertNodeLO(root, 4)
root = insertNodeLO(root, 5)
root = insertNodeLO(root, 6)
root = insertNodeLO(root, 7)

result = []
postOrder(root, result)
print(result)
