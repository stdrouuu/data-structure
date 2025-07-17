import sys 

class Vertex:
    def __init__(self,node):
        self.id = node
        self.adjacent = {}
        self.distance = sys.maxsize
        self.visited = False
        self.previous = None 

    def addNeighbor(self,neighbor,weight = 0):
        self.adjacent[neighbor] = weight

    def getConnection(self):
        return self.adjacent.keys()
    
    def getVertexid(self):
        return self.id
    
    def getWeight(self,neighbor):
        return self.adjacent[neighbor]
    
    def setDistance(self,dist):
        self.distance = dist

    def getDistance(self):
        return self.distance

    def setPrevious(self,prev):
        self.previous = prev
    
    def setVisited(self):
        self.visited = True
    
    def __str__(self):
        return str(self.id) + 'adjacent' + str([x.id for x in self.adjacent])
        
class Graph:
    def __init__(self):
        self.vertDict = {}
        self.numVert = 0

    def __iter__(self):
        return iter(self.vertDict.values())
    
    def addVertex(self,node):
        self.numVert = self.numVert + 1
        newVert = Vertex(node)
        self.vertDict[node] = newVert
        return newVert
    
    def getVertex(self,n):
        if n in self.vertDict:
            return self.vertDict[n]
        else:
            return None
        
    def addEdge(self, frm, to, cost = 0):
        if frm not in self.vertDict:
            self.addVertex(frm)
        if to not in self.vertDict:
            self.addVertex(to)

        self.vertDict[frm].addNeighbor (self.vertDict[to], cost)
        self.vertDict[to].addNeighbor (self.vertDict[frm], cost)

    def getVertices(self):
        return self.vertDict.keys()
    
    def setPrevious(self,current):
        self.previous = current

    def getPrevious(self,current):
        return self.previous

    def getEdges(self):
        edges = []
        for v in G:
            for w in v.getConnection():
                vid = v.getVertexid()
                wid = w.getVertexid()
                edges.append((vid, wid, v.getWeight(w)))
        return edges
    
if __name__ == "__main__":
    G = Graph ()
    G.addVertex ('a')
    G.addVertex ('b')
    G.addVertex ('c')
    G.addVertex ('d')
    G.addVertex ('e')
    print("Graph data:")
    G.addEdge("a","e",10)
    G.addEdge("a","c",12)
    G.addEdge("c","b",30)
    G.addEdge("b","e",40)
    G.addEdge("e","d",50)
    
    print(G.getEdges())
