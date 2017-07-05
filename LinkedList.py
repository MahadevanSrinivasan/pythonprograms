import sys

class Node:
  def __init__(self, data):
    self.val = data
    self.nextNode = None


class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  
  def insert(self, data):
    node = Node(data)
    if not self.head:
      self.head = node
      self.tail = node
    else:
      node.nextNode = self.head
      self.head = node

  def printList(self):
    curr = self.head
    while curr:
      print curr.val,
      curr = curr.nextNode

  def insertAtEnd(self, data):
    node = Node(data)
    if not self.tail:
      self.head = node
      self.tail = node
    else:
      self.tail.nextNode = node
      self.tail = node

  def partition(self, p):
    p1 = self.head
    p2 = self.head

    while p2 and p1:
      while p1 and p1.val < p:
        p1 = p1.nextNode

      if p2 == self.head:
        p2 = p1

      while p2 and p2.val >= p:
        p2 = p2.nextNode

      if p1 and p2:
        (p1.val, p2.val) = (p2.val, p1.val)

  def partition2(self, p):
    lnew = LinkedList()
    curr = self.head
    while curr:
      if curr.val < p:
        lnew.insert(curr.val)
      else:
        lnew.insertAtEnd(curr.val)
      curr = curr.nextNode

    self.head = lnew.head
    self.tail = lnew.tail

  def isPalindrome2(self):
    slow = self.head
    fast = self.head
    stack = []
    while fast and fast.nextNode:
      stack.append(slow.val)
      slow = slow.nextNode
      fast = fast.nextNode.nextNode

    if fast:
      slow = slow.nextNode
    
    while slow:
      if slow.val != stack.pop():
        return False
      slow = slow.nextNode
    
    return True

  def isPalindrome(self): 
    rev = self.reverse()
    revhead = rev.head
    curhead = self.head
    while curhead and revhead:
      if curhead.val != revhead.val:
        return False
      curhead = curhead.nextNode
      revhead = revhead.nextNode
    return True

  def reverse(self):
    lnew = LinkedList()
    curr = self.head
    while curr:
      lnew.insert(curr.val)
      curr = curr.nextNode
    return lnew

if __name__ == '__main__':
  alist = [1, 2, 10, 5, 8, 5, 3]
  l = LinkedList()
  for elem in alist:
    l.insert(elem)
  print 'Partition with element 5'
  l.partition2(5)
  l.printList()
  print 'Reversing list'
  r = l.reverse()
  r.printList()
  print 'Is Palindrome?', l.isPalindrome2()
  print 'New list:'
  l = LinkedList()
  l.insert(0)
  l.insert(1)
  l.insert(2)
  l.insert(1)
  l.insert(0)
  l.printList()
  print 'Is Palindrome?', l.isPalindrome2()
