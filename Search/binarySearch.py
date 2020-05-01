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

# print(binarySearch([3,4,5,56,78],78))


def rec_binarySearch(arr,ele):
    
  l= 0 
  r = len(arr)-1

  mid = (l+r)//2 

  if len(arr) == 0:
    print("false")
    return False

  if arr[mid] == ele:
    print('true')
    return True
  
  if ele < arr[mid]:
    # print(arr[:mid-1])
    rec_binarySearch(arr[:mid],ele)
  if ele > arr[mid]:
    # print(arr[mid+1:])
    rec_binarySearch(arr[mid+1:],ele)    



print(rec_binarySearch([3,4,5,56,78],78))