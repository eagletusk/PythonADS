# tree traversals

result = []

def inorder(tree):
  if tree:
    inorder(tree.getLeftVal())
    result.append(tree.getRootVal)
    inorder(tree.getLeftVal()))

def sort_check(arr):
  for i in range(1,len(arr)-1,1):
    if i-1 > i:
      return False
  return True

inorder(tree)
sort_check(result)



# tree traversals

result = []

def preorder(tree,level):
  level +=1
  if tree:
    result.append((level,tree.getRootVal))
    preorder(tree.getLeftVal(),level)
    preorder(tree.getLeftVal(),level)



preorder(tree, 0)