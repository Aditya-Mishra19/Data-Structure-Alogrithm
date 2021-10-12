def selectionSort(arr):
    for i in range(len(arr)):    
        min_ele_index= i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_ele_index]:
                min_ele_index = j      
        # Swapping
        arr[i], arr[min_ele_index] = arr[min_ele_index], arr[i]

# Driver Code
arr= eval(input()) #Enter input in list
selectionSort(arr)
print(arr)

""" 
TC- O(n^2) for both worst & best case.
SC- O(1)
"""