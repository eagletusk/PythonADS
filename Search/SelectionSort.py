import random

def selection(arr):

  for fillslot in range(len(arr)-1,0,-1):
    posMax = 0

    for location in range (1, fillslot+1 ):
      if arr[location] > arr[posMax]:
        posMax = location

    temp = arr[fillslot] 
    arr[fillslot] = arr[posMax]
    arr[posMax] = temp

  return arr


arr = [random.randint(0,6) for i in range(6)]
print(arr)
print(selection(arr))