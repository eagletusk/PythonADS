class BT(object):

  def __init(self,rootObj):
    
    self.key =rootObj
    self.leftChild = None
    self.rightChild = None
  
  def insertLeft(self,newNode):
    if self.leftChild = None
      self.leftChild = BT(newNode)
    else:
      t = BT(newNode)
      t.leftChild = self.leftChile
      self.leftChild = t

  def insertright(self,newNode):
    if self.rightChild = None
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