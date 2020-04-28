#
class Node(object):
  def __init__(self,value):
    self.value = value
    self.nextnode = None


class DNode(object):
  def __init__(self,value):
    self.value = value
    self.nextnode = None
    self.prevnode = None


a = Node(1)
b = Node(2)

a.nextnode = b

c = DNode(1)
d = DNode(2)
e = DNode(3)

c.nextnode = d
d.nextnode = e

d.prevnode = c
e.prevnode = d

print(d)