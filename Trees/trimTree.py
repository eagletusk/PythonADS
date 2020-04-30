class Node(object):
  def __init__(self,value):
    self.val = value
    self.left = None
    self.right = None

count = 0
def trimbst(tree,minVal,maxVal,count):
  count +=1
  if not tree:
    print('here',count)
    return
 
  tree.left = trimbst(tree.left,minVal,maxVal,count)
  tree.right = trimbst(tree.right,minVal,maxVal,count)


  print(tree.val,count)
  if minVal <= tree.val <= maxVal:
    return tree
  
  if tree.val < minVal:
    return tree.right 

  if tree.val> maxVal:
    return tree.left


r = Node(12)
r.right = Node(23)
r.left = Node(5)
r.left.left = Node(2)
r.left.left.left = Node(1)
r.left.right= Node(3)
r.right.left = Node(22)
r.right.right = Node(100)

trimbst(r,4,88,0)


