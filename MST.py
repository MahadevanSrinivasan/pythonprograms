import sys
from EdgeWeightedGraph import EdgeWeightedGraph
from MinPQ import MinPQ

class MST:
  def __init__(self, G):
    self.marked = {}
    for vid in G.getVertexIds():
      self.marked[vid] = False
    self.edges = []
    self.pq = MinPQ()
    self.weight = 0

    self.visit(G, 0)
    while not self.pq.isEmpty():
      edge = self.pq.delMin()
      v = edge.either()
      w = edge.other(v)
      if self.marked[v] and self.marked[w]:
        continue
      if not self.marked[v]:
        self.visit(G, v)
      if not self.marked[w]:
        self.visit(G, w)
      self.edges.append(edge)
      self.weight += edge.getWeight()

  def visit(self, G, vid):
    self.marked[vid] = True
    edges = G.getAdjacentEdges(vid)
    for edge in edges:
      if not self.marked[edge.other(vid)]:
        self.pq.insert(edge)
    
  def getEdges(self):
    return self.edges

  def getWeight(self):
    return self.weight


if __name__ == '__main__':
  inputFile = sys.argv[1]
  g = EdgeWeightedGraph(inputFile)
  mst = MST(g)

  for e in mst.getEdges():
    print e

  print mst.getWeight()
