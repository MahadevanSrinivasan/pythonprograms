import sys
from Graph import Graph

UNDISCOVERED = 0
DISCOVERED = 1
PROCESSED = 2
class Cycle:
  def __init__(self, G):
    self.vertexState = {}
    self.parent = {}
    for vid in G.getVertexIds():
      self.vertexState[vid] = UNDISCOVERED
      self.parent[vid] = None
    self.cycle = False
    for s in G.getVertexIds():
      if self.vertexState[vid] == UNDISCOVERED:
        self.dfs(G, s, s)
  
  # search vertex and its parent vertex
  def dfs(self, G, s, p):
    src = G.getVertex(s)
    self.processVertexEarly(s)
    self.vertexState[s] = DISCOVERED
    for n in src.getNeighbors():
      if self.vertexState[n] == UNDISCOVERED:
        self.parent[n] = s
        self.processEdge(s, n)
        self.dfs(G, n, s)
      # If we have discovered this vertex before
      # and if it not the current vertex's parent
      # then we have a cycle
      elif n != p:
        print "Cycle detected while visiting edge", s, " -> ", n
        self.cycle = True
    self.processVertexLate(s)
    self.vertexState[s] = PROCESSED
  
  def processVertexEarly(self, s):
    print "Discovered vertex ", s
    return
  
  def hasCycle(self):
    return self.cycle

  def processVertexLate(self, s):
    return
  
  def processEdge(self,s, n):
    print "Processed Edge ", s, " -> ", n
    return

if __name__ == '__main__':
  inputFile = sys.argv[1]
  g = Graph(inputFile)
  d = Cycle(g)
  print "Has cycle = ", d.hasCycle()
