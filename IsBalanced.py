from BST import BST
import random




if __name__ == '__main__':
  N = int(sys.argv[1])
  b = BST()
  for i in range(N):
    v = random.random()
    b.putValue(v, i)


