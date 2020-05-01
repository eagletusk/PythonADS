def bubble(arr):

    for i in range(len(arr)-1,0,-1):
      for k in range(i):
        print(range(i))
        if arr[k]>arr[k+1]:
          temp = arr[k]
          arr[k] = arr[k+1]
          arr[k+1] = temp
    
    return arr

print(bubble([1,4,3,2,1]))