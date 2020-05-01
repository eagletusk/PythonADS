class HashTable(object):
  def __init__(self):
    self.size = size
    self.slots = [None] * self.size

  def put(self,key,data):
    hashvalue = self.hashfunction(key,len(self.slots))
    if self.slots[hashvalue] == None:
      self.slots[hashValue] = key
      self.data[hashValue] = data
    else:

      if self.slots[hashvalue] == key:
        self.data[hashValue] = data

      else:
        nextslot = self.rehash(hasvalue,len(self.slots))

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
    return (oldhash+1)%size



  def get(self, key):

  def del(self,ket):

  len
  in

  def __len__(self):
    return