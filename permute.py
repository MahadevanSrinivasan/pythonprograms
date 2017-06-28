import sys

def permute(s):
  if len(s) == 0:
    return []
  elif len(s) == 1:
    return [s]
  else:
    perms = []
    for i in range(len(s)):
      for p in permute(s[0:i] + s[i+1:]):
        perms.append(s[i] + p)
    return perms

if __name__ == '__main__':
  if len(sys.argv) == 2:
    permute(sys.argv[1])
