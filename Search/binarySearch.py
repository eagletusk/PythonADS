def binarySearch(arr,ele):

  l= 0 
  r = len(arr)-1
  found = False


  while l <= r:

    mid = (l+r)//2 

    if arr[mid] == ele:
      return True
    
    if ele < arr[mid]:
      r = mid-1
    if ele > arr[mid]:
      l = mid +1
  return False

print(binarySearch([3,4,5,56,78],78))
