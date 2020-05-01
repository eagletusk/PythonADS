import random

def bubbles(arr):

  for n in range(len(arr)-1,0,-1):
    for k in range(0,n):

      if arr[k] > arr[k+1]:
        temp = arr[k+1]
        arr[k+1] = arr[k]
        arr[k] = temp

  return arr

arr = [random.randint(0,10) for i in range (10)]
print(arr)
print(bubbles(arr))