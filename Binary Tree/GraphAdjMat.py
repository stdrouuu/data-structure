class Vertex:
    def __init__(self,node):
        self.id = node
        self.visited = False

    def getVertexid(self):
        return self.id
    
    def setVertexid(self,id):
        self.id = id

    def setVisited(self):
        self.visited = True

    def getConnection(self, G):
        return G.adjMatrix[self.id]
    
    def addNeighbor(self,neighbor,G):
        G.addEdge(self.id, neighbor)

    def __str__(self):
        return str(self.id)
    
class Graph:
    def __init__(self, numVert, cost = 0):
        self.adjMatrix = [[-1] * numVert for _ in range(numVert)]
        self.numVert = numVert
        self.vertices = [] 
        for i in range(0, numVert):
            newVert = Vertex(i) 
            self.vertices.append(newVert)

    def setVertex(self, vtx, id):
        if 0 <= vtx < self.numVert:
            self.vertices[vtx].setVertexid(id)

    def getVertex(self, n):
        for vertin in range(0, self.numVert):
            if n == self.vertices[vertin].getVertexid():
                return vertin
        return -1
        
    def addEdge(self, frm, to, cost = 0): 
        if self.getVertex(frm) != -1 and self.getVertex(to) != -1:
            self.adjMatrix[self.getVertex(frm)][self.getVertex(to)] = cost
            self.adjMatrix[self.getVertex(to)][self.getVertex(frm)] = cost

    def getVertices(self):
        vertices = []
        for vertin in range(0, self.numVert):
            vertices.append(self.vertices[vertin].getVertexid())
        return vertices
    
    def printMatrix(self):
        for u in range(0, self.numVert):
            row = []
            for v in range (0, self.numVert):
                row.append(self.adjMatrix[u][v])
            print (row)

    def getEdges(self):
        edges = []
        for v in range(0, self.numVert):
            for u in range(0, self.numVert):
                if self.adjMatrix[u][v] != -1:
                    vid = self.vertices[v].getVertexid()
                    wid = self.vertices[u].getVertexid()
                    edges.append((vid, wid, self.adjMatrix[u][v]))
        return edges
    
if __name__ == "__main__":
    G = Graph (5)
    G.setVertex (0,"a")
    G.setVertex (1,"b")
    G.setVertex (2,"c")
    G.setVertex (3,"d")
    G.setVertex (4,"e")
    print("Graph data:")
    G.addEdge("a","e",10)
    G.addEdge("a","c",12)
    G.addEdge("c","b",30)
    G.addEdge("b","e",40)
    G.addEdge("e","d",50)
    G.addEdge("f","e",60)
    print (G.printMatrix())
    print(G.getEdges())
