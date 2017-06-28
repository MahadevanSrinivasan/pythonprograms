import sys
import random

class MaxPQ:

  def __init__(self):
    self.values = [None]
    self.count = 0

  def insert(self, v):
    self.values.append(v)
    self.count += 1
    self.swim(self.count)

  def delMax(self):
    temp = self.values[1]
    self.values[1] = self.values[self.count]
    self.values.pop()
    self.count -= 1
    self.sink(1)
    return temp
  
  def isEmpty(self):
    return self.count == 0

  def swim(self, i):
    while i > 1:
      p = i // 2
      if self.values[p] < self.values[i]:
        (self.values[p], self.values[i]) = (self.values[i], self.values[p])
      else:
        break
      i = i // 2

  def sink(self, i):
    while 2*i <= self.count:
      c = 2*i
      c1 = 2*i + 1
      if c1 <= self.count and self.values[c] < self.values[c1]:
        c = c1

      if self.values[i] < self.values[c]:
        (self.values[i], self.values[c]) = (self.values[c], self.values[i])
      else:
        break

      i = c

if __name__ == '__main__':
  N = int(sys.argv[1])
  pq = MaxPQ()
  for i in range(N):
    pq.insert(random.randint(1, 99))
    print pq.values

  while(not pq.isEmpty()):
    print pq.delMax()
