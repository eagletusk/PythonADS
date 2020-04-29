class BT(object):

  def __init__(self,rootObj):
    
    self.key =rootObj
    self.leftChild = None
    self.rightChild = None
  
  def insertLeft(self,newNode):
    if self.leftChild == None:
      self.leftChild = BT(newNode)
    else:
      t = BT(newNode)
      t.leftChild = self.leftChild
      self.leftChild = t

  def insertRight(self,newNode):
    if self.rightChild == None:
      self.rightChild = BT(newNode)
    else:
      t = BT(newNode)
      t.rightChild = self.rightChild
      self.rightChild = t

  def getRightChild(self):
    return self.rightChild

  def getLeftChild(self):
    return self.leftChild

  def setRootVal(self,obj):
    self.key = obj

  def getRootVal(self):
    return self.key

r = BT('a')
print(r.getRootVal())
print(r.getRightChild())
r.insertLeft(3)
r.insertLeft(2)
r.insertRight(4)
print(r.getLeftChild().getRootVal())