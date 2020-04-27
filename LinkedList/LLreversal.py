class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None

def reverse(head):
  current = head
  prev = None
  nextt = None

  while current:
    # Copy the current nodes next node to a variable next_node
    # Before overwriting as the previous node for reversal
    nextnode = current.nextnode

    # Reverse the pointer ot the next_node
    current.nextnode = prev
    # Go one forward in the list
    prev = current
    current = nextnode
    print(current)
  return prev
  
  


      


# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d    

print (a.nextnode.value)
print (b.nextnode.value)
print (c.nextnode.value)

reverse(a)

print (a.value)
print (b.value)
print (c.value)

print ("d",d.nextnode.value)
print (c.nextnode.value)
print (b.nextnode.value)