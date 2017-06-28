def binarysearch(l, s):
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
  return -1
      

if __name__ == "__main__":
  assert(binarysearch([], 3) == -1)
  assert(binarysearch([1], 3) == -1)
  assert(binarysearch([1], 1) == 0)
  assert(binarysearch([1, 3, 5], 1) == 0)
  assert(binarysearch([1, 3, 5], 3) == 1)
  assert(binarysearch([1, 3, 5], 5) == 2)
  assert(binarysearch([1, 3, 5], 0) == -1)
  assert(binarysearch([1, 3, 5], 2) == -1)
  assert(binarysearch([1, 3, 5], 4) == -1)
  assert(binarysearch([1, 3, 5], 6) == -1)
  assert(binarysearch([1, 3, 5, 7], 1) == 0)
  assert(binarysearch([1, 3, 5, 7], 3) == 1)
  assert(binarysearch([1, 3, 5, 7], 5) == 2)
  assert(binarysearch([1, 3, 5, 7], 7) == 3)
  assert(binarysearch([1, 3, 5, 7], 0) == -1)
  assert(binarysearch([1, 3, 5, 7], 2) == -1)
  assert(binarysearch([1, 3, 5, 7], 4) == -1)
  assert(binarysearch([1, 3, 5, 7], 6) == -1)
  assert(binarysearch([1, 3, 5, 7], 8) == -1)
