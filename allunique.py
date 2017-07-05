import sys

def isAllUnique(s):
  d = {}
  for i in range(len(s)):
    if s[i] in d:
      return False
    else:
      d[s[i]] = True
  return True


if __name__ == '__main__':
  s = sys.argv[1]
  print 'Is (', s, ')all unique', isAllUnique(s)
