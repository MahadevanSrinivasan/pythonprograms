import sys

def permute2(s):
  if not s: 
    yield "" 
  else:
    for i in range(len(s)):
      for p in permute2(s[0:i] + s[i+1:]):
        yield (s[i] + p)

if __name__ == '__main__':
  if len(sys.argv) == 2:
    p = permute2(sys.argv[1])
