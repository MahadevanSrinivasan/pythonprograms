import sys
from Digraph import Digraph

UNDISCOVERED = 0
DISCOVERED = 1
PROCESSED = 2
class DirectedDFS:
  def __init__(self, G, s):
    self.vertexState = {}
    self.parent = {}
    for vid in G.getVertexIds():
      self.vertexState[vid] = UNDISCOVERED
      self.parent[vid] = None
    self.count = 0
    self.source = s
    self.dfs(G, s)
    
  def dfs(self, G, s):
    self.count += 1
    src = G.getVertex(s)
    self.processVertexEarly(s)
    self.vertexState[s] = DISCOVERED
    for n in src.getNeighbors():
      if self.vertexState[n] == UNDISCOVERED:
        self.parent[n] = s
        self.processEdge(s, n)
        self.dfs(G, n)
    self.processVertexLate(s)
    self.vertexState[s] = PROCESSED
  
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
  
  def getCount(self):
    return self.count
  
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
  g = Digraph(inputFile)
  d = DirectedDFS(g, sourceId)

  for vid in g.getVertexIds():
    print sourceId, "to", vid, ":",
    print d.pathTo(vid)
  print ""
  
 # if d.getCount() == g.getNoOfVertices():
 #   print "connected"
 # else:
 #   print "NOT connected"
  

