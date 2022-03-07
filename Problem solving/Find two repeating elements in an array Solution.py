def findRepeating(arr,n):
    x=0
    y=0
    xor=arr[0]
    for i in range(1,n): #This gives value X
        xor^=arr[i]
    for i in range(1,n-1):# This gives value Y
        xor^=i
    #Now XOR contains the X XOR Y
    #get the right most bit number
    set_no=(xor) & ~(xor-1)

    #divide the elements into 2 groups based on the right most set bit
    for i in range(n):
        if arr[i] & set_no: #we are calculating for set bit for array 
            x^=arr[i]
        else:
            y^=arr[i]
    for i in range(1,n-1): #we are calculating for set bit for numbers from 1 to m 
        if i & set_no:
            x^=i
        else:
            y^=i
    return x,y

if __name__=='__main__':
    arr=[4, 2, 4, 5, 3, 3, 1]
    x,y=findRepeating(arr,len(arr))
    print(x,y)

