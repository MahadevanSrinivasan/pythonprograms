import random

def rowColToCellNum(r, c):
  return (r*8) + c

def isValidRowCol(r, c):
  if(r >= 0 and r < 8 and c >= 0 and c < 8):
    return True
  else:
    return False

def getClosedCells(openCells, currentCell):
  r = currentCell // 8
  c = currentCell % 8
  
  closedCells = []
  
  for i in range(-7, 8):
    newCol = c + i
    newRow = r + i
    # Same row is blocked
    if isValidRowCol(r, newCol):
      closedCells.append(rowColToCellNum(r, newCol))

    # Same column is blocked
    if isValidRowCol(newRow, c):
      closedCells.append(rowColToCellNum(newRow, c))

    # Right diagonal
    if isValidRowCol(newRow, newCol):
      closedCells.append(rowColToCellNum(newRow, newCol))

    newCol = c + i
    newRow = r - i
    if isValidRowCol(newRow, newCol):
      closedCells.append(rowColToCellNum(newRow, newCol))
  
  closedCells = set(closedCells)
  # Only the common cells are the "newly" closed cells
  closedCells = closedCells & openCells
  return closedCells


def nqueens(n, path, limit, openCells):
  openCellsList = list(openCells)
  if(len(openCellsList) == 0):
    return (False, path)
  
  openCellsList = list(openCells)
  choice = openCellsList[0] # random.choice(openCellsList)
  path.append(choice)
  closedCells = getClosedCells(openCells, choice)
  openCells = openCells - closedCells

  if n < limit:
    done = False
    i = 0

    while i < len(openCells) and not done:
      (done, temp) = nqueens(n+1, path, limit, openCells)
      i = i + 1

    if not done:
      path.pop()
      openCells = openCells | closedCells

  else:
    done = True

  return (done, path)

if __name__ == '__main__':
  openCells = set(range(64))
  (done, soln) = nqueens(1, [], 8, openCells) 
  for i in range(8):
    for j in range(8):
      if((i*8)+j in soln):
        print 'Q ',
      else:
        print '- ',
    print "\n"


