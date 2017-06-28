import sys
from Graph import Graph

UNDISCOVERED = 0
DISCOVERED = 1
PROCESSED = 2
class BreadthFirstSearch:
  def __init__(self, G, s):
    self.vertexState = {}
    self.parent = {}
    for vid in G.getVertexIds():
      self.vertexState[vid] = UNDISCOVERED
      self.parent[vid] = None
    self.count = 0
    self.source = s
    self.bfs(G, s)
    
  def bfs(self, G, s):
    q = [s]
    self.vertexState[s] = DISCOVERED
    while len(q) != 0:
      self.count += 1
      s = q.pop(0)
      src = G.getVertex(s)
      self.processVertexEarly(s)
      for n in src.getNeighbors():
        if self.vertexState[n] == UNDISCOVERED:
          self.parent[n] = s
          self.processEdge(s, n)
          q.append(n)
          self.vertexState[n] = DISCOVERED
      self.processVertexLate(s)
      self.vertexState[s] = PROCESSED

  def getCount(self):
    return self.count

  def hasPathTo(self, v):
    return self.vertexState[v] != UNDISCOVERED
    
  def pathTo(self, v):
    s = []
    if self.hasPathTo(v):
      s.insert(0, v)
      while self.parent[v]:
        v = self.parent[v]
        s.insert(0, v)
      if v != self.source:
        s.insert(0, self.source)
    return s 

  def processVertexEarly(self, s):
    #print "Discovered vertex ", s
    return
    
  def processVertexLate(self, s):
    return
  
  def processEdge(self,s, n):
    #print "Processed Edge ", s, " -> ", n
    return

if __name__ == '__main__':
  inputFile = sys.argv[1]
  sourceId = int(sys.argv[2])
  g = Graph(inputFile)
  b = BreadthFirstSearch(g, sourceId)
  
  for vid in g.getVertexIds():
    print sourceId, "to", vid, ":", 
    if b.hasPathTo(vid):
      print b.pathTo(vid)
  
  print ""
  
  if b.getCount() == g.getNoOfVertices():
    print "connected"
  else:
    print "NOT connected"
  

