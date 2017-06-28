import sys

class Vertex:
  def __init__(self, id):
    self.id = id
    self.neighbors = []
  
  def addNeighbor(self, vid):
    self.neighbors.insert(0, vid)
  
  def getNeighbors(self):
    return self.neighbors

  def __str__(self):
    return str(self.neighbors)

  __repr__ = __str__

class Digraph:
  def __init__(self, inputFile, V=0):
    self.vertices = {}
    self.noOfVertices = V
    self.noOfEdges = 0
    if inputFile:
      f = open(inputFile, "r")
      self.noOfVertices = int(f.readline());
      self.noOfEdges = int(f.readline());
      for i in range(self.noOfEdges):
        edge = f.readline().split(' ')
        self.addEdge(int(edge[0]), int(edge[1]))

  def addVertex(self, u):
    self.vertices[u] = Vertex(u)

  def addEdge(self, u, v):
    if(u not in self.vertices):
      self.addVertex(u)
    if(v not in self.vertices):
      self.addVertex(v)
    
    self.vertices[u].addNeighbor(v)
  
  def getVertexIds(self):
    return self.vertices.keys()
  
  def getVertex(self, id):
    return self.vertices[id]
  
  def getNoOfVertices(self):
    return self.noOfVertices

  def getNoOfEdges(self):
    return self.noOfEdges

  def reverse(self):
    d = Digraph(None, self.noOfVertices)
    for vid in self.getVertexIds():
      v = self.getVertex(vid)
      for neighbor in v.getNeighbors():
        d.addEdge(neighbor, vid)
    return d
 
if __name__ == '__main__':
  inputFile = sys.argv[1]
  g = Digraph(inputFile)
  for v in g.getVertexIds():
    print v, g.getVertex(v).getNeighbors()

  r = g.reverse()
  for v in r.getVertexIds():
    print v, r.getVertex(v).getNeighbors()

