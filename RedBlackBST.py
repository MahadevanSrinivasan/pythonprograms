import sys
import random

RED = True
BLACK = False

class Node:
  def __init__(self, key, val, N, color):
    self.key = key
    self.val = val
    self.N   = N
    self.left = None
    self.right = None
    self.color = color

# Note: Deletion is not implemented
class RedBlackBST:
  def __init__(self):
    self.root = None
  
  def getSize(self):
    return self.getSizeHelper(self.root)
  
  def getSizeHelper(self, node):
    if node:
      return node.N
    else:
      return 0
  
  def isRed(self, node):
    if not node:
      return False
    return node.color == RED

  def rotateLeft(self, node):
    x = node.right
    node.right = x.left
    x.left = node
    x.color = node.color
    node.color = RED
    x.N = node.N
    node.N = self.getSizeHelper(node.left) + self.getSizeHelper(node.right) + 1
    return x

  def rotateRight(self, node):
    x = node.left
    node.left = x.right
    x.right = node
    x.color = node.color
    node.color = RED
    x.N = node.N
    node.N = self.getSizeHelper(node.left) + self.getSizeHelper(node.right) + 1
    return x
  
  def flipColors(self, node):
    node.color = RED
    node.left.color = BLACK
    node.right.color = BLACK

  def getValue(self, key):
    return self.getValueHelper(self.root, key)
  
  def getValueHelper(self, root, key):
    if not root:
      return None
    if root.key < key:
      return self.getValueHelper(root.right, key)
    elif root.key > key:
      return self.getValueHelper(root.left, key)
    else:
      return root.val
      
  def putValueHelper(self, root, key, val):
    if not root:
      return Node(key, val, 1, RED)

    if root.key < key:
      root.right = self.putValueHelper(root.right, key, val)
    elif root.key > key:
      root.left = self.putValueHelper(root.left, key, val)
    else:
      root.val = val
    
    if self.isRed(root.right) and (not self.isRed(root.left)):
      root = self.rotateLeft(root)
    if self.isRed(root.left) and self.isRed(root.left.left):
      root = self.rotateRight(root)
    if self.isRed(root.left) and self.isRed(root.right):
      self.flipColors(root)
    root.N = self.getSizeHelper(root.left) + self.getSizeHelper(root.right) + 1
    return root
  
  def putValue(self, key, val):
    print 'Inserting key, val pair', key, val
    self.root = self.putValueHelper(self.root, key, val)
    self.root.color = BLACK

  def inorderTraversal(self):
    q = []
    q = self.inorderTraversalHelper(self.root, q)
    return q

  def inorderTraversalHelper(self, root, q):
    if root:
      q = self.inorderTraversalHelper(root.left, q)
      q.append(root.key)
      q = self.inorderTraversalHelper(root.right, q)
    return q
  
  def getAllKeys(self):
    return self.getKeys(self.getMinKey(), self.getMaxKey())

  def getKeys(self, lo, hi):
    q = []
    q = self.getKeysHelper(self.root, q, lo, hi)
    return q

  def getKeysHelper(self, root, q, lo, hi):
    if root:
      if root.key >= lo:
        q = self.getKeysHelper(root.left, q, lo, hi)
      if root.key >= lo and root.key <= hi:
        q.append(root.key)
      if root.key <= hi:
        q = self.getKeysHelper(root.right, q, lo, hi)
    return q

  def getMinKey(self):
    minNode = self.getMinKeyHelper(self.root)
    if minNode:
      return minNode.key
    else:
      return None

  def getMinKeyHelper(self, root):
    if not root:
      return None

    if root.left:
      return self.getMinKeyHelper(root.left)
    else:
      return root

  def getMaxKey(self):
    return self.getMaxKeyHelper(self.root)

  def getMaxKeyHelper(self, root):
    if not root:
      return None

    if root.right:
      return self.getMaxKeyHelper(root.right)
    else:
      return root.key

  def getFloor(self, key):
    x = self.getFloorHelper(self.root, key)
    if not x:
      return None
    return x.key

  def getFloorHelper(self, root, key):
    if not root:
      return None

    if root.key > key:
      return self.getFloorHelper(root.left, key)
    elif root.key < key:
      node = self.getFloorHelper(root.right, key)
      if node:
        return node

    return root

  def getCeil(self, key):
    x = self.getCeilHelper(self.root, key)
    if not x:
      return None
    return x.key

  def getCeilHelper(self, root, key):
    if not root:
      return None

    if root.key < key:
      return self.getCeilHelper(root.right, key)
    elif root.key > key:
      node = self.getCeilHelper(root.left, key)
      if node:
        return node

    return root
  
  def select(self, rank):
    node = self.selectHelper(self.root, rank)
    if node:
      return node.key
    return None

  def selectHelper(self, root, rank):
    if not root:
      return None
  
    t = self.getSizeHelper(root.left)
    if t > rank:
      return self.selectHelper(root.left, rank)
    elif t == rank:
      return root
    else:
      return self.selectHelper(root.right, rank-t-1)

  def getRank(self, key):
    return self.getRankHelper(self.root, key)

  def getRankHelper(self, root, key):
    if not root:
      return None

    t = self.getSizeHelper(root.left)
    # Number of keys on the left subtree is the rank
    if root.key == key:
      return t 
    # If given key is less than root's key, search left subtree recursively
    elif root.key > key:
      return self.getRankHelper(root.left, key)
    # If given key is larger than root's key, left and root are both less than key
    # Find out how many we have on the right side also and add all of them
    else:
      return t + 1 + self.getRankHelper(root.right, key)
  
   
if __name__ == '__main__':
  b = RedBlackBST()
  numElems = int(sys.argv[1])
  arr = []
  for i in range(numElems):
    v = random.randint(1, 99)
    arr.append(v)
    b.putValue(v, i)
  
  print 'Inorder Traversal', b.inorderTraversal()
  print 'Get all keys', b.getAllKeys()
  print 'Get keys between 1 and 50', b.getKeys(1, 50)
  print 'Get min key', b.getMinKey()
  print 'Get max key', b.getMaxKey()
  r = random.randint(1, 99)
  print 'Floor of', r, '=', b.getFloor(r)
  print 'Ceil of', r, '=', b.getCeil(r)
  r = random.randint(0, numElems)
  s = b.select(r)
  print 'Select of', r, '=', s
  print 'Rank of', s, '=', b.getRank(s)
