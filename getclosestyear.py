import math
import sys

def getClosestYear(inyear):
  currentyear = 2016
  inyear = int(inyear)
  option1 = 1900 + inyear
  option2 = 2000 + inyear
  if (abs(option1 - currentyear) > abs(option2 - currentyear)):
    outyear = option2
  else:
    outyear = option1
  return outyear

if __name__ == '__main__':
  if(len(sys.argv) == 2):
    print getClosestYear(sys.argv[1])
