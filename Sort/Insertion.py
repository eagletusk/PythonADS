print ('insertion')

def insertion_sort(arr):
  print(arr)
  for i in range(1,len(arr)):

    currentvalue = arr[i]
    position = i

    # check the edge case of position going past 0
    # check the edge case of the current value being greater than the what has been sorted

    # dont go past Zero
    # if the currentValue is less than the position -1 then shift it donw until you hit a smaller value. 
    while position > 0 and arr[position -1] > currentvalue:
      
      # swap the values 
      arr[position] = arr[position-1]
      position = position-1
      
    # replace the final value 
    arr[position] = currentvalue


arr = [3,8,5,3,4,5,63345,44]
insertion_sort(arr)
print(arr)