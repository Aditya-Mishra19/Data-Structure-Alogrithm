# Python code for Bubble sort.
def bubbleSort(arr):                
    for i in range (len(arr)):
        for j in range (len(arr)-i-1):
            if arr[j] > arr[j+1]:              # Comaparing the element
                arr[j], arr[j+1] = arr[j+1], arr[j]  # swaps the element

# Driver code
arr= [1, 10, 3, 2, 11, 5]
bubbleSort(arr)             # calling function
print(arr)

# Time complexcity ; Worst case [O(n^2)], Best case [O(n)]
# Space complexcity ; O(1)