class Node(object):
  def __init__(self,value):

    self.value = value
    self.next = None
    self.previous = None

a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
b.previous = a
c.previous = b
c.next = a
a.previous = c
print(a.next.value, a.previous.value, a.value)
print (a.value)