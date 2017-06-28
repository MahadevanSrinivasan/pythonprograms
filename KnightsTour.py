from Graph import Graph

def posToNodeId(row, col, boardSize):
  return ((row * boardSize) + col)

def knightGraph(boardSize):
  ktGraph = Graph()
  for row in range(boardSize):
    for col in range(boardSize):
      posMoves = genLegalMoves(row, col, boardSize)
      nodeId = posToNodeId(row, col, boardSize)
      for posMove in posMoves:
        ktGraph.addEdge(nodeId, posToNodeId(posMove[0], posMove[1], boardSize))

  return ktGraph

def legalCoord(i, boardSize):
  return ((i >= 0 and i < boardSize))

def genLegalMoves(row, col, boardSize):
  newMoves = []
  moveOffsets = [(-1, -2), (-1,  2), (-2, -1), (-2, 1),
                 ( 1, -2), ( 1,  2), ( 2, -1), ( 2, 1)]
  
  for offset in moveOffsets:
    newX = (row + offset[0])
    newY = (col + offset[1])
    if legalCoord(newX, boardSize) and \
       legalCoord(newY, boardSize):
       newMoves.append((newX, newY))
    
  return newMoves

def orderByAvail(n):
  resList = []
  for v in n.getConnections():
    if(v.getColor() == 'white'):
      c = 0
      for w in v.getConnections():
        if w.getColor() == 'white':
          c += 1
        resList.append((c, v))
  resList.sort(key=lambda x: x[0])
  return [y[1] for y in resList]

def knightTour(n, path, u, limit):
  u.setColor('gray')
  path.append(u)
  
  if n < limit:
    nbrList = orderByAvail(u) # list(u.getConnections())
    done = False
    i = 0
    while(i < len(nbrList) and not done):
      if(nbrList[i].getColor() == 'white'):
        done = knightTour(n+1, path, nbrList[i], limit)
      i = i + 1
    if not done:
      path.pop()
      u.setColor('white')
  else:
    done = True

  return done
      

if __name__ == '__main__':
  size = 5
  g = knightGraph(size)
  v = g.getVertices()
  path = []
  knightTour(1, path, g.getVertex(v[0]), size**2 - 2)
  print path
