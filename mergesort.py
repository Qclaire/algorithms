def Merge(arr1, arr2):
    l1 =  len(arr1) # length of first array
    l2 =  len(arr2) # length of second array
    p1 = 0; p2 = 0  # pointers to begining of both
    arr = [] # the result array
    
    # if either pointer exceeds the length of its corresponding array, we stop!
    while p1 < l1 and p2 < l2:
      # compare and add the lesser value to the result
      # increment the corresponding pointer
        if arr1[p1] > arr2[p2]: 
            arr.append(arr2[p2])
            p2 += 1
        else:
            arr.append(arr1[p1])
            p1 += 1
    
    # the while loop breaks after the shorter array is exhausted
    # since we don't know which one was shorter we check whick pointer equals length of its corresponding array
    # then empty the remaining content into the result array
    if p1 == l1:
        arr = arr + arr2[p2:]
    else:
        arr =  arr +  arr1[p1:]
    
    return arr
  

def MergeSort(arr):
  if len(arr) > 1:
    mid = len(arr)//2
    a = MergeSort(arr[:mid])
    b = MergeSort(arr[mid:])
    return Merge(a, b)
  return arr
    
print(MergeSort([10,9,8,7,6,5,4,3,2,1]))