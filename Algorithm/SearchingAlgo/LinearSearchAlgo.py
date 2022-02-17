# your code goes here
def search(arr, x): 
  
    for i in range(len(arr)): 
  
        if arr[i] == x: 
            return i 
  
    return -1
    
result = search([10, 20, 80, 30, 60, 50, 110, 100, 130, 170], 110)
if result == -1:
	print("Element Not found")
else:
	print("Eleement found")