def searchforwords(wordmatrix):
  visited = [[False, False, False],
             [False, False, False],
             [False, False, False]];
  for i in range(len(wordmatrix)):
    for j in range(len(wordmatrix[0])):    
      searchforwordshelper(wordmatrix, visited, "", i, j)

def isValidCell(x, y, xlen, ylen):
  if((x >= 0) and (x < xlen) and (y >= 0) and (y < ylen)):
    return True
  else:
    return False

def findNextMoves(wordmatrix, visited, i, j):
  nextMoves = []
  moveOffsets = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)];
  xlen = len(wordmatrix)
  ylen = len(wordmatrix[0])

  for offset in moveOffsets:
    newX = i + offset[0]
    newY = j + offset[1]
    if(isValidCell(newX, newY, xlen, ylen)):
       nextMoves.append((newX, newY))
  return nextMoves

def searchforwordshelper(wordmatrix, visited, currword, i, j):
  visited[i][j] = True
  currword = currword + wordmatrix[i][j]
  if(isword(currword)):
    print currword
  nextmoves = findNextMoves(wordmatrix, visited, i, j)
  for nm in nextmoves:
    if(visited[nm[0]][nm[1]] == False):
      searchforwordshelper(wordmatrix, visited, currword, nm[0], nm[1])
  
  # Done with letter at (i, j) - Clear visited so it can be used in another path 
  visited[i][j] = False
  currword = currword[:-1]

def isword(word):
  words = {'geeks', 'for', 'quiz', 'go', 'geek', 'kze'}
  if(word in words):
    return True
  else:
    return False

if __name__ == '__main__':
  wordmatrix = [['g', 'i', 'z'],
                ['u', 'e', 'k'],
                ['q', 's', 'e']];
  searchforwords(wordmatrix) 
