import sys
import random
from BST import BST
'''
Perfect Balance - Sedgewick 3.2.25
'''

def PerfectBalance(b, arr):
  arr = sorted(arr)
  return PerfectBalanceHelper(b, arr, 0, len(arr)-1)

def PerfectBalanceHelper(b, arr, lo, hi):
  if lo > hi:
    return b
  mid = lo + (hi - lo)//2
  b.putValue(arr[mid], mid)
  b = PerfectBalanceHelper(b, arr, lo, mid-1)
  b = PerfectBalanceHelper(b, arr, mid+1, hi)
  return b
  
  
if __name__ == '__main__':
  N = int(sys.argv[1])
  arr = []
  for i in range(N):
    v = random.random()
    arr.append(v)
  
  b = BST()
  b = PerfectBalance(b, arr)
  # Check the height of the BST
  print 'Height of the perfect tree = ', b.getHeight()
  # Check if balanced
  print 'Is tree balanced?', b.isBalanced()
