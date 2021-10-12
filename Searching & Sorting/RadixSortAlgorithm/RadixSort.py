def countingSort(arr, place):
    n = len(arr)
    count = [0]*10
    result = [0]*n
    # Calculate count of each elements
    for i in range (n):
        index = arr[i] // place
        count[index % 10] += 1
    # Calculate cummulative sum
    for i in range (1,10):
        count[i] += count[i-1]
    #place the element in sorted order
    i = n - 1
    while i >= 0:
        index = arr[i] // place
        result[count[index % 10]-1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    # Copying the element in the array
    for i in range (n):
        arr[i] = result[i]

def radixSort(arr):
    #find max element
    max_element = max(arr)
    #apply counting sort to sort element's based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(arr,place)
        place *= 10

# Driver Code
arr = eval(input()) # Enter the element in list format
radixSort(arr)
print(arr)

"""
TC = O(N*D)
SC = O(1)
"""