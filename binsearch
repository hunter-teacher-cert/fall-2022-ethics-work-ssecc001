def binarySearch(array, num):
    low = 0
    high = len(array) - 1
    middle = 0 #use this instead of current index
  
    while low <= high:
 
        middle = (high + low) // 2
 
        # If num is greater, ignore left side
        if array[middle] < num:
            low = middle + 1
 
        # If num is smaller, ignore right side
        elif array[middle] > num:
            high = middle - 1
 
        # means num is the midde number
        else:
            return middle
 
    # If we reach here, then the number is not in the list
    return -1
 
 

array = [ 3, 5, 10, 22, 50]
num = 10lss
 
result = binarySearch(array, num)
 
if result != -1:
    print("Number is present at index " +  str(result))
else:
    print("Number is not present in array")
