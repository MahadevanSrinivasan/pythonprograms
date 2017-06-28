import sys

def counts2(n):
  div = 5
  count = 0
  while(n % div != n):
    count += ((n / div))
    div = div * 5 
  return count

def counts(n):
  evens = 0
  fives = 0
  tens = 0
  for i in range(1, n+1):
    temp = i
    while(temp % 10 == 0):
      tens += 1
      temp = temp / 10
    while(temp % 5 == 0):
      fives += 1
      temp = temp / 5
    while(temp % 2 == 0):
      evens += 1
      temp = temp / 2
  
  return tens + min(evens, fives)


if __name__ == '__main__':
  print counts2(int(sys.argv[1]))
