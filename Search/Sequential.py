def seq_search(arr,ele):
  pos =0 
  found = False

  while pos < len(arr) and not found:

    if arr[pos] == ele:
      found = True
    else:
      pos +=1
  print(found)
  return found

arr = [2,3,4,5]
ele = 4

seq_search(arr,ele)