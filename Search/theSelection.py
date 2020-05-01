import random

def theSelection(arr):

  print(list(range(len(arr)-1,-1,-1)))
  for n in range(len(arr)-1,-1,-1):
    maxpos = 0
    for k in range(0,n+1):
      if arr[k] > arr[maxpos]:
        maxpos = k
      
      temp = arr[n]
      arr[n] = arr[maxpos]
      arr[maxpos] = temp

  return arr


arr = [random.randint(1,88) for _ in range(10)]
print(arr)
print(theSelection(arr))

