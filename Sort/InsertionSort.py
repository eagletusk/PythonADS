def ins(arr):

  for i in range(1,len(arr)):

    curVal = arr[i]

    while i>0 and arr[i-1] > curVal:

      arr[i] = arr[i-1]
      i = i -1

  arr[i] = curVal

arr= [1,4,5,7,4,3,-20,4.55]
ins(arr)
print(arr)