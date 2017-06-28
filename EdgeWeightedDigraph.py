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

class DirectedEdge:
  def __init__(self, v, w, weight):
    self.v = v
    self.w = w
    self.weight = weight

  def getWeight(self):
    return self.weight

  def fromvertex(self):
    return self.v

  def tovertex(self):
    return self.w

  def __cmp__(self, other):
    if self.getWeight() < other.getWeight():
      return -1
    elif self.getWeight() > other.getWeight():
      return 1
    else:
      return 0

  def __str__(self):
    return str(self.v) + " " + str(self.w) + " " + str(self.weight)

  __repr__ = __str__

class EdgeWeightedDigraph:
  def __init__(self, inputFile):
    self.vertices = {}
    self.noOfVertices = 0
    self.noOfEdges = 0
    f = open(inputFile, "r")
    self.noOfVertices = int(f.readline());
    self.noOfEdges = int(f.readline());
    for i in range(self.noOfEdges):
      edge = f.readline().split(' ')
      self.addEdge(int(edge[0]), int(edge[1]), float(edge[2]))

  def addVertex(self, u):
    self.vertices[u] = Vertex(u)

  def addEdge(self, u, v, weight):
    if(u not in self.vertices):
      self.addVertex(u)
    if(v not in self.vertices):
      self.addVertex(v)
    
    self.vertices[u].addNeighbor(DirectedEdge(u, v, weight))
  
  def getVertexIds(self):
    return self.vertices.keys()
  
  def getVertex(self, id):
    return self.vertices[id]
  
  def getNoOfVertices(self):
    return self.noOfVertices

  def getNoOfEdges(self):
    return self.noOfEdges

  def getEdges(self):
    edges = []
    for vid in self.getVertexIds():
      for e in self.getAdjacentEdges(vid):
         edges.append(e)
    return edges

  def getAdjacentEdges(self, v):
    return self.vertices[v].getNeighbors()
 
if __name__ == '__main__':
  inputFile = sys.argv[1]
  g = EdgeWeightedDigraph(inputFile)
  for v in g.getVertexIds():
    print v, g.getAdjacentEdges(v) 

  print g.getEdges()
  
