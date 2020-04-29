import collections

class Node(object):
  def __init__(self,val=None):
    self.left = None
    self.right = None
    self.val = val


d = collections.deque([1,2,3])



def levelOrderPrint(tree):
  ten = []
  if not tree:
    return

  nodes = collections.deque([tree])

  current_count =1
  next_count = 0


  while len(nodes) != 0:
    currentNode = nodes.popleft()
    current_count -=1
    
    print(currentNode.val ,'', end = '')

    if currentNode.left:
      nodes.append(currentNode.left)
      next_count +=1

    if currentNode.right:
      nodes.append(currentNode.right)
      next_count +=1

    if current_count == 0:
      print('\n')
      current_count, next_count = next_count, current_count

    
   

root = Node(2)
root.left = Node(1)
root.right = Node(4)
root.left.left = Node(2)
root.left.right = Node(4442)
levelOrderPrint(root)