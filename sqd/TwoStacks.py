class Queue2Stacks(object):    
    def __init__(self):
        
        # Two Stacks
        self.stack1 = []
        self.stack2 = []
     
    def enqueue(self,element):
        self.stack1.append(element)
        # FILL OUT CODE HERE
        pass
    
    def dequeue(self):
        if not self.stack2:

          while self.stack1:
            print(self.stack1)
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
        # FILL OUT CODE HERE


"""
RUN THIS CELL TO CHECK THAT YOUR SOLUTION OUTPUT MAKES SENSE AND BEHAVES AS A QUEUE
"""
q = Queue2Stacks()

for i in range(0,5,1):
    q.enqueue(i)
    
for i in range(0,5,1):
    print (q.dequeue())