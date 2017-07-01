def rank(l, s):
  lo = 0
  hi = len(l) - 1
  while(lo <= hi):
    mid = (hi - lo)/2 + lo
    if(l[mid] == s):
      return mid
    elif(l[mid] < s):
      lo = mid + 1
    else:
      hi = mid - 1
  return lo

if __name__ == "__main__":
  assert(rank([], 3) == 0)
  assert(rank([1], 3) == 1)
  assert(rank([1], 1) == 0)
  assert(rank([1, 3, 5], 1) == 0)
  assert(rank([1, 3, 5], 3) == 1)
  assert(rank([1, 3, 5], 5) == 2)
  assert(rank([1, 3, 5], 0) == 0)
  assert(rank([1, 3, 5], 2) == 1)
  assert(rank([1, 3, 5], 4) == 2)
  assert(rank([1, 3, 5], 6) == 3)
  assert(rank([1, 3, 5, 7], 1) == 0)
  assert(rank([1, 3, 5, 7], 3) == 1)
  assert(rank([1, 3, 5, 7], 5) == 2)
  assert(rank([1, 3, 5, 7], 7) == 3)
  assert(rank([1, 3, 5, 7], 0) == 0)
  assert(rank([1, 3, 5, 7], 2) == 1)
  assert(rank([1, 3, 5, 7], 4) == 2)
  assert(rank([1, 3, 5, 7], 6) == 3)
  assert(rank([1, 3, 5, 7], 8) == 4)
