import sys

def OneAway(str1, str2):
  N = len(str1)
  M = len(str2)
  if abs(N - M) > 1:
    return False
  
  if N == M:
    return SubCheck(str1, str2)
  elif N > M:
    return InsDelCheck(str1, str2)
  else:
    return InsDelCheck(str2, str1)

def InsDelCheck(str1, str2):
  N = len(str1)
  M = len(str2)
  shift = 0
  for i in range(M):
    if str1[i] != str2[i]:
      shift += 1
    else:
      break
    if shift > 1:
      return False

  diff = 0
  i = 0
  while i < M:
    if str1[shift] != str2[i]:
      diff += 1
    else:
      i += 1
    shift += 1
    if diff > 1:
      return False

  return True

def SubCheck(str1, str2):
  cost = 0
  N = len(str1)
  for i in range(N):
    if str1[i] != str2[i]:
      cost += 1
    if cost > 1:
      return False
  return True

def UnitTests():
  assert(OneAway('pale', 'ple') == True)
  assert(OneAway('pales', 'pale') == True)
  assert(OneAway('bale', 'pale') == True)
  assert(OneAway('pale', 'bae') == False)

if __name__ == '__main__':
  UnitTests()
