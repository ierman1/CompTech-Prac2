def find_max_rec(lst):
    '''documentation'''

    # Base case, length == 1
    # We return the only element in the list as a result, even if its a negative integer
    # The start index is inclusive, while the end index is exclusive (thus, we always retrun 0,0,lst[0])
    if len(lst) == 1 :
        return 0, 0, lst[0]
    
    #Recursive case. I we get here, we initialize a pivot
    pivot = len(lst) // 2
    
    #Call the recursive function with each side as a parameter
    left = find_max_rec(lst[:pivot])
    right = find_max_rec(lst[pivot:])

    #To obtain the maximum result from the center outwards, we first calculate the maximum on the left side and on the right side
    #We call those values leftMaxAccum and rightMaxAccum

    leftAccum = 0
    leftMaxAccum = 0
    leftIndex = pivot #We initialize leftIndex as pivot, in case all left values are negative
    i = pivot-1
    while i >= 0 :
        leftAccum += lst[i]
        if leftAccum >= leftMaxAccum:
            leftMaxAccum = leftAccum
            leftIndex = i
        i -= 1 #The loop goes from the center to the left
    
    rightAccum = 0
    rightMaxAccum = 0
    rightIndex = pivot
    i = pivot
    while i < len(lst) :
        rightAccum += lst[i]
        if rightAccum >= rightMaxAccum:
            rightMaxAccum = rightAccum
            rightIndex = i
        i += 1 #The loop goes from center to the right

    #To determine the center maximum value, we pick the left index as starting index
    center = leftIndex, rightIndex, leftMaxAccum + rightMaxAccum

    if left[2] >= center[2] and left[2] >= right[2] :
        #left is the max
        return left

    #if left isn't the max, only the right and center can be
    elif right[2] >= center[2] :
        #right is the max
        return [pivot+right[0], pivot+right[1], right[2]]
    else:
        #center is the max
        return center


print(find_max_rec([2, -4, 1, 9, -6, 7, -3]))
print(find_max_rec([2, 2, 1, -9, -7, 7, -3]))