def BinarySearch(arr:list, k:int)->bool:
    "Returns True or false\n\n may be tweaked to return the exact location \n\n arr must be sorted in ascending order"
    

    if not arr or (len(arr)==1 and arr[0]!=k):
        return "NA"

    half =  len(arr)//2
    if k == arr[half]:
        return "found"
    elif k < arr[half]:
        return BinarySearch(arr[:half],k)
    else:
        return BinarySearch(arr[half:],k)
print(BinarySearch([],4))
