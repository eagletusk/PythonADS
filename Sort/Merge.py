def merge(arr):

  if len(arr)>1:

    mid = len(arr)//2
    print (mid)
    left = arr[:mid]
    right = arr[mid:]

    merge(left)
    merge(right)

    i = 0 
    j = 0 
    k = 0 

    while i < len(left) and j < len(right):

      if left[i] < right[j]:
        arr[k] = left[i]
        i = i +1
      else:
        arr[k] = right[j]
        j += 1

      k+=1
        
    
    while i < len(left) :
      arr[k] = left[i]
      i += 1
      k += 1

    while j < len(right):
      arr[k] = right[j]
      j+=1
      k+=1

    print(arr)

arr = [2,4444,3,33,444,565,4433,5672.4,3]
merge(arr)
print(arr)
