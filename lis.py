import sys
import random

def LIS(alist):
  lis_at_index = [1]*len(alist)
  prev_at_index = [None]*len(alist)
  curr_best_end = 0

  for curr_index in range(1, len(alist)):
    for prev_index in range(curr_index):
      if lis_at_index[prev_index] + 1 > lis_at_index[curr_index] and alist[curr_index] > alist[prev_index]:
         lis_at_index[curr_index] = lis_at_index[prev_index] + 1
         prev_at_index[curr_index] = prev_index
    if lis_at_index[curr_index] > lis_at_index[curr_best_end]:
      curr_best_end = curr_index

  print lis_at_index
  print prev_at_index
  
  lis = [alist[curr_best_end]]
  while prev_at_index[curr_best_end] != None:
    lis.insert(0, alist[prev_at_index[curr_best_end]])
    curr_best_end = prev_at_index[curr_best_end]
  return lis

if __name__ == '__main__':
  alist = [2,4,3,5,1,7,6,9,8]
  print LIS(alist)
