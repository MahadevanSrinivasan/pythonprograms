import sys
import random

class Node:
  def __init__(self, key, val, N):
    self.key = key
    self.val = val
    self.N   = N
    self.left = None
    self.right = None
'''
This BST implementation is almost entirely based on Algorithms 4th Edition by
Sedgewick and Wayne. There are differences because of the absence of overloading
in Python. Where applicable, there are also mentions of  exercise problem
numbers. It also includes a driver which creates a random tree and exercises
some of the methods involved.
'''  
class BST:
  def __init__(self):
    self.root = None
  
  def getSize(self):
    return self.getSizeHelper(self.root)
  
  def getSizeHelper(self, node):
    if node:
      return node.N
    else:
      return 0
  
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
      return Node(key, val, 1)

    if root.key < key:
      root.right = self.putValueHelper(root.right, key, val)
    elif root.key > key:
      root.left = self.putValueHelper(root.left, key, val)
    else:
      root.val = val
    
    root.N = self.getSizeHelper(root.left) + self.getSizeHelper(root.right) + 1
    return root
  
  def putValue(self, key, val):
    self.root = self.putValueHelper(self.root, key, val)

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
  
  def getRoot(self):
    return self.root
  
  # Sedgewick Exercise 3.2.37
  def printLevel(self, node):
    if not node:
      return
    
    q = [node]
    while q:
      currnode = q.pop()
      print currnode.key,
      if currnode.left:
        q.insert(0, currnode.left)
      if currnode.right:
        q.insert(0, currnode.right)
    
    print ""
  
  # Sedgewick Exercise 3.2.7
  def getHeight(self):
    return self.getHeightRecursive(self.root)
    
  def getHeightRecursive(self, root):
    if not root:
      return -1
    
    return max(self.getHeightRecursive(root.left), 
               self.getHeightRecursive(root.right)) + 1 
  
  def isBalanced(self):
    if not self.root:
      return True

    return abs(self.getHeightRecursive(self.root.left) - self.getHeightRecursive(self.root.right)) <= 1

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
  
  def delMin(self):
    if not self.root:
      return None
    else:
      self.root = self.delMinHelper(self.root)
        
  def delMinHelper(self, root):
    if not root:
      return None
    
    # Can't go anymore to the left
    if not root.left:
      return root.right
    else:
      root.left = self.delMinHelper(root.left)
      root.N = self.getSizeHelper(root.left) + self.getSizeHelper(root.right) + 1
      return root
  
  def delKey(self, key):
    self.root = self.delKeyHelper(self.root, key)
  
  def delKeyHelper(self, root, key):
    if not root:
      return None
      
    if root.key < key:
      root.right = self.delKeyHelper(root.right, key)
    elif root.key > key:
      root.left = self.delKeyHelper(root.left, key)
    # Found the key
    else:
      # If it only has one child it is a simple operation
      if not root.left:
        return root.right
      elif not root.right:
        return root.left
      # If it has both children, it is more complicated
      # Save the key to be deleted
      t = root
      # Let us find its successor, it is the min of the right subtree
      root = self.getMinKeyHelper(t.right)
      # Right subtree needs to be replaced by key being deleted's right
      # after deleting the minimum (which is the successor again)
      root.right = self.delMinHelper(t.right)
      # Successor is bound to have an empty left tree 
      # Just overwrite with left tree of key being deleted
      root.left = t.left

    root.N = self.getSizeHelper(root.left) + self.getSizeHelper(root.right) + 1
    return root
   
if __name__ == '__main__':
  b = BST()
  numElems = int(sys.argv[1])
  arr = []
  for i in range(numElems):
    v = random.randint(1, 99)
    arr.append(v)
    print 'Inserting key, val pair', v, i
    b.putValue(v, i)
  
  print 'Inorder Traversal', b.inorderTraversal()
  print 'Levelorder Traversal'
  b.printLevel(b.getRoot())
  print 'Height of the tree', b.getHeight()
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
  print 'Deleting min'
  b.delMin()
  print 'Inorder Traversal after delMin', b.inorderTraversal()
  r = random.randint(1, 99)
  print 'Delete a random key', r
  b.delKey(r)
  print 'Inorder Traversal after random deletion', b.inorderTraversal()
  print 'Delete a key in the tree', arr[2]
  b.delKey(arr[2])
  print 'Inorder Traversal after deletion', b.inorderTraversal()
  print 'Levelorder Traversal'
  b.printLevel(b.getRoot())
  print 'Is the tree balanced?', b.isBalanced()
