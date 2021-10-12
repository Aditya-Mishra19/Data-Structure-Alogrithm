def countingSort(arr):
    n = len(arr)
    max_ele = max(arr)
    count = [0]*(max_ele+1)
    result = [0]*n
    # 1. Storing the count of each element in count array.
    for i in range(n):
        count[arr[i]] += 1

    # 2. Store the cummulative sum of count array.
    for i in range(1, max_ele+1):
        count[i] += count[i-1]
    
    """ 
    3. Find the index of each element of the original array, in count array 
       and place the element's resultant array.
    """

    i = n -1
    while i >= 0:
        result[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1
        i -= 1
    for i in range (n):
        arr[i] = result[i]

#Driver code.
arr = eval(input()) #Enter the input in list format
countingSort(arr)
print(arr)