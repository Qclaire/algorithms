
def hourglassSum(arr:list)->int:
    """forms hour-glasses from 2d arr, returns max sum of glasses"""
    sums = []
    for row in range(len(arr)-2):# go row-by-row to the end, since glass is 3 cols long
        for col in range(len(arr)-2): # then col-by-col
            top = sum((arr[row][col], arr[row][col+1], arr[row][col+2])) # get the top of the glass and sum
            mid = arr[row+1][col+1] # get the single midle val 
            bot = sum((arr[row+2][col], arr[row+2][col+1], arr[row+2][col+2])) # get the bottom of the glass and sum
            sums.append(bot + top + mid) # add to the sums arr
    return(max(sums))# find the max sum and return
