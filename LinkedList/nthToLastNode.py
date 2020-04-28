class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode  = None

# def nth_to_last_node(n, head):
#     # print(head.value)
#     next_node = head
#     prev_node = []
#     while next_node != None:
#       prev_node.append(next_node)
#       next_node = next_node.nextnode
    
#     # print (prev_node)
#     lenn = len(prev_node)-1 
#     nth = lenn -n 
#     return prev_node[nth+1]

def nth_to_last_node(n,head):
  
  left = head
  right = head

  for i in range(n-1):

    if not right.nextnode:
      raise LookupError('Error n is larger')

    right = right.nextnode
    
  while right.nextnode :

    left = left.nextnode
    right = right.nextnode

  return left

"""
RUN THIS CELL TO TEST YOUR SOLUTION AGAINST A TEST CASE 

PLEASE NOTE THIS IS JUST ONE CASE
"""

from nose.tools import assert_equal

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

####

class TestNLast(object):
    
    def test(self,sol):
        
        assert_equal(sol(2,a),d)
        print ('ALL TEST CASES PASSED')
        
# Run tests
t = TestNLast()
t.test(nth_to_last_node)