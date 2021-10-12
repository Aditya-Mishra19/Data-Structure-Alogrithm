# Implementing Merge Sort algorithm

def merge(arr, left, right):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j] :
            arr[k] = left[i]
            i += 1
        else:
            arr[k]  = right[j]
            j += 1
    k += 1

    # if element is still left in left array or right array ( Adding Infinity case )
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[ : mid]
        right = arr[ mid : ]
        mergeSort(left)
        mergeSort(right)
        merge( arr, left, right)

# Driver code
arr= [56, 24, 9, 38, 98, 66]
mergeSort(arr)
print(arr)

# TC - O(nlogn)