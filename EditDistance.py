import sys

def EditDistance(s1, s2):
  m = len(s1)
  n = len(s2)
  dp = []
  dp = [[0 for i in range(n+1)] for j in range(m+1)]
  ptr = [['****' for i in range(n+1)] for j in range(m+1)]
  
  for i in range(m+1):
    for j in range(n+1):
      # First string is empty, second string has j characters
      # Edit distance is j deletes/inserts
      if i == 0:
        dp[i][j] = j
      # Second string is empty, first string has i characters
      # Edit distance is i deletes/inserts
      elif j == 0:
        dp[i][j] = i
      
      else:
        # Note: dp[i][j] holds the edit distance for s1[0:i], s2[0:j]
        # s1[0:i] -> characters from 0 to i-1 (inclusive)
        insert_cost = dp[i][j-1] + 1
        delete_cost = dp[i-1][j] + 1
        # Substitution cost is 0 if the characters are same, assume they are the same first
        sub_cost    = dp[i-1][j-1]
        # If these two chars are not same, then substitution cost is 2 
        if s1[i-1] != s2[j-1]:
          sub_cost += 2
        (dp[i][j], ptr[i][j]) = minPath(insert_cost, delete_cost, sub_cost)
  for i in dp:
    print i

  for i in ptr:
    print i
  computePath(ptr, m, n)

  return dp[m][n]

def minPath(i, d, s):
  minVal = min(min(i, d), s)

  if minVal == s:
    minPath = 'diag'
  elif minVal == d:
    minPath = 'down'
  else:
    minPath = 'left'

  return (minVal, minPath)

def computePath(ptr, m, n):
  if ptr[m][n] == 'diag':
    print 'S',
    m = m - 1
    n = n - 1
  elif ptr[m][n] == 'left':
    print 'I',
    m = m - 1
  else:
    print 'D',
    n = n - 1
  if n <= 0 or m <= 0:
    return
  computePath(ptr, m, n)

def printOperation(dp, m, i, j):
  if m == (-1, 0):
    print 'D',
  elif m == (0, -1):
    print 'I',
  else:
    if dp[i][j] != dp[i-1][j-1]:
      print 'S',
    else:
      print '*',

if __name__ == '__main__':
  print 'Strings:', sys.argv[1], sys.argv[2]
  print EditDistance(sys.argv[1], sys.argv[2])
