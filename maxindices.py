def maxindices(lst):
  maxval = -10000
  for i in range(len(lst)):
    if(lst[i] > maxval):
      maxval = lst[i]

  for i in range(len(lst)):
    if(lst[i] == maxval):
      yield i


for i in maxindices([1, -2, 0, 6, 2, -4, 6, 6]):
  print i
