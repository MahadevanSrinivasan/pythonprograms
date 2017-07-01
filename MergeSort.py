import sys
import random

class MergeSort:
  def __init__(self, a):
    self.compares = 0
    self.a = a
  
  def doSort(self):
    self.mergesorthelper(0, len(self.a)-1)
    
  def getCompares(self):
    return self.compares
  
  def getResult(self):
    return self.a
  
  def isSorted(self):
    isSorted = True
    for i in range(len(self.a)-1):
      if self.a[i] > self.a[i+1]:
        return False
    return isSorted

  def mergesorthelper(self, lo, hi):
    # Gotcha: lo == hi for base case (single element)
    if lo == hi:
      return
    # mid computed this way for avoid overflow
    mid = lo + (hi - lo) // 2
    # Sort elements from lo to mid (inclusive)
    self.mergesorthelper(lo, mid)
    # Sort elements from mid+1 to hi (inclusive)
    self.mergesorthelper(mid+1, hi)
    # Merge them. Mid needed to split
    self.merge(lo, mid, hi)
  
  def merge(self, lo, mid, hi):
    # Create lower array lo to mid (inclusive)
    # Gotcha: Slicing needs mid+1
    b = self.a[lo:mid+1]
    # Create upper array mid+1 to hi (inclusive)
    # Gotcha: Slicing needs hi+1
    c = self.a[mid+1:hi+1]
    # Sentinel large numbers so as to avoid extra checks
    b.append(float('inf'))
    c.append(float('inf'))
    bindex = 0
    cindex = 0
    # Use lo to index into original array
    # Copy only hi - lo + 1 elements
    while lo <= hi:
      if b[bindex] < c[cindex]:
        self.a[lo] = b[bindex]
        bindex += 1
      else:
        self.a[lo] = c[cindex]
        cindex += 1
      self.compares += 1
      lo += 1

if __name__ == "__main__":
  N = int(sys.argv[1])
  alist = []
  for i in range(N):
    alist.append(random.random())
  m = MergeSort(alist)
  m.doSort()
  print 'After sort: Is array sorted?', m.isSorted()
  print 'Number of compares', m.getCompares()
