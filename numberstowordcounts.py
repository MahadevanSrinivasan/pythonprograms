uniquewords = {1: "one", 2: "two", 3:"three", 4:"four", 5:"five",
               6: "six", 7: "seven", 8:"eight", 9:"nine", 10: "ten",
               11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
               15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
               19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
               60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety", 100: "hundred",
               1000: "thousand"}
allLengths = [None] * 1001
count = 0
for (key, val) in uniquewords.iteritems():
  allLengths[key] = len(val)

for i in xrange(1, 1001):
  q = None
  r = None
  if(not allLengths[i]):
    if(i < 100):
      q = int(i / 10)
      r = i % 10
      allLengths[i] = allLengths[q*10] + allLengths[r]
    else:
      q = int(i / 100)
      r = i % 100
      if(r == 0):
        allLengths[i] = allLengths[q] + allLengths[100]
      else:
        allLengths[i] = allLengths[q*100] + allLengths[r] + 3
  count = count + allLengths[i]
  print i, allLengths[i], count

print count
