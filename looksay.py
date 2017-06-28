import sys

def looksayseq(n):
  l = ["1", "11"]
  for i in range(2, n):
    prev = l[-1]
    l.append("")
    count = 1
    for j in range(1, len(prev)):
      if prev[j-1] == prev[j]:
        count += 1
      else:
        l[-1] = l[-1] + str(count) + prev[j-1]
        count = 1
    print j
    l[-1] = l[-1] + str(count) + prev[j]
  print l
        

if __name__ == '__main__':
  looksayseq(int(sys.argv[1]))
