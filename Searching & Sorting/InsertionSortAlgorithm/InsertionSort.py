# Python program for Insertion sort algorithm.

#Function for insertion sort
def InsertionSort (arr):
    for i in range (1, len(arr)):
        key = arr[i]
        # insert arr[i] into sorted arr[1,2,..., i-1]
        j = i - 1
        while j >= 0 and arr[j] > key :
            arr[j + 1] = arr[j]
            j = j -1
        arr[j+1] = key

# Driver code to test above
arr = [50, 30, 40, 10, 20]
InsertionSort(arr) #calling ins ertion sort function 
print("Sorted array : ")
for result in arr:
    print(result, end= " ") #print all sorted element in a row with space

# This code is contributed by Aditya Mishra  