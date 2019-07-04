# NOt so efficient. see below for better
def smallestMode(array:list) -> int:
    """a solution for the hackerank challenge, Migratory birds"""
    s = set(array)
    count = 0
    val = 0
    for i in s:
        c = array.count(i)
        if c>count:
            count = c
            val = i

    return val


# Most Efficient Solution
def smallestMode(array:list) -> int:
    out = [0]*max(array) # intialise and array with lenght equal max size of the given array
    for i in  array:
       out[i] +=1
    return out.index(max(out))
smallestMode([1,4,2,2,5,3])
