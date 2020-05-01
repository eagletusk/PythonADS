class HashTable(object):
  def __init__(self,size):
    self.size = size
    self.slots = [None] * self.size
    self.data = [None]*self.size

  def put(self,key,data):
    hashvalue = self.hashfunction(key,len(self.slots))
    if self.slots[hashvalue] == None:
      self.slots[hashvalue] = key
      self.data[hashvalue] = data
      # print('here 1')
    else:
      # print('here2')
      if self.slots[hashvalue] == key:
        self.data[hashvalue] = data
        # print('here 3')
      else:
        nextslot = self.rehash(hashvalue,len(self.slots))
        # print('here4')
        while self.slots[nextslot] != None and self.slots[nextslot] != key:
          nextslot = self.rehash(nextslot,len(self.slots))
        
        if self.slots[nextslot] == None:
          self.slots[nextslot] = key
          self.data[nextslot] = data
        else:
          self.data[nextslot] = data
          


  def hashfunction(self,key,size):
    # remainder method
    return key%size

  def rehash(self, oldhash, size):
    print("rehash")
    return (oldhash+1)%size

  def get (self,key):
    startslot = self.hashfunction(key,len(self.slots))
    data = None
    stop = False
    found = False
    position = startslot

    while self.slots[position] != None and not found and not stop: 

      if self.slots[position] == key:
        found = True
        data = self.dat[position]

      else: 
        position = self.rehash(position,len(self.slots))
        if position == startslot:
          stop = True
    return data



  def __getitem__(self,key):
    return self.get(key)

  def __setitem__(self,key,data):
    self.put(key,data)
  

h = HashTable(5)
h[1] = "one"
h[3] = 'three'
print(h.data)

# for x in [ i for i in range(20)]:
#   print (x%5,x)


h.put(0,"yoyo")
print(h.data)

h.put(10,"yoyos")
print(h.data)

