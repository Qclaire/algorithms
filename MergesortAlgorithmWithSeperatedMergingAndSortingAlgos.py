def mergeSortedArrays(left_half, right_half):
    i = 0 # counter for right side of the array
    j = 0 # for the other side
    k = 0
    """ if we set a tracker, we can tell which array was last picked from"""
    """as the loop breaks when shorter one is exhausted, we can add all remaining elements in other array"""
    track = None; # keeping track of which side we picked from on each pick
    arr = [] # the output array

    """ if one array is empty return the other since it is sorted"""
    if right_half and not left_half: 
        return right_half
    if left_half and not right_half:
        return left_half
    
    """if both are empty then the sorted array is empty"""
    if not left_half and not right_half:
        return []
    """ now iterate n times => l(shorter arr) on both arrays"""
    while i<len(left_half) and j<len(right_half):
        """since both arrays are sorted, the first element in each is the least"""
        """the least amont the two is the least in the final array, and goes in first"""
        if left_half[i] < right_half[j]:# compare 1st i and j
            arr.append(left_half[i])
            i += 1 # incremetn right counter
            track = 1 # set the tracker to 1
        else:
            arr.append(right_half[j])
            j += 1
            track = 2 # set the tracker to 2
        k += 1
    """for uneven arr len one array will have elements unappended to the final array"""
    """lets use the tracker to see where we last picked from, then we know the other array to continue"""
    if track == 1: # left hand was last selected from
        return arr + right_half[j:] # add all element in right half starting from the last index we selected
    elif track == 2: # same as above
        return arr + left_half[i:]
    
def mergeSort(arr):
    if len(arr)==1:
        return arr
    
    else:
        half = len(arr)//2
        
        right = arr[:half]
        left = arr[half:]
        
        return mergeSortedArrays(mergeSort(right), mergeSort(left))

#print(mergeSort([3,2,1,0,5,90,1,4,65,23,4]))
