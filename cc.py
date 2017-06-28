import sys
from Graph import Graph

UNDISCOVERED = 0
DISCOVERED = 1
PROCESSED = 2
class CC:
  def __init__(self, G):
    self.vertexState = {}
    self.parent = {}
    for vid in G.getVertexIds():
      self.vertexState[vid] = UNDISCOVERED
      self.parent[vid] = None
    self.count = 0
    self.componentIds = [0 for i in range(G.getNoOfVertices())]
    for s in G.getVertexIds():
      if self.vertexState[s] == UNDISCOVERED:
        self.dfs(G, s)
        self.count += 1
    
  def dfs(self, G, s):
    self.componentIds[s] = self.count
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
 
  def connected(self, v, w):
    return self.componentIds[v] == self.componentIds[w]
 
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
  g = Graph(inputFile)
  cc = CC(g)
  print cc.getCount(), "components"
  components = []
  for i in range(cc.getCount()):
    components.append([])

  for vid in g.getVertexIds():
    components[cc.componentIds[vid]].append(vid)

  for i in range(cc.getCount()):
    print components[i]
  

