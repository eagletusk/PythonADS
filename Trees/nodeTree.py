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

  def preorder(self):
    if self.key:
      print(self.key)
      if self.leftChild:
        self.leftChild.preorder()
      if self.rightChild:
        self.rightChild.preorder()


r = BT('a')
# print(r.getRootVal())
# print(r.getRightChild())
r.insertLeft(3)
r.insertLeft(2)
r.insertRight(4)
# print(r.getLeftChild().getRootVal())

r.preorder()


def preorder(tree):
  if tree:
    print(tree.getRootVal())
    preorder(tree.getLeftChild())
    preorder(tree.getRightChild())

def postorder(tree):
  if tree:
    postorder(tree.getLeftChild())
    postorder(tree.getRightChild())
    print(tree.getRootVal())