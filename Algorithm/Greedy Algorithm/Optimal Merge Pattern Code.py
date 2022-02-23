import heapq

def optimalMerge(files):
    heapq.heapify(files)
    count = 0
    while len(files) > 1:
        first = heapq.heappop(files)
        second = heapq.heappop(files)
        
        temp = first + second
        
        count = count + temp
        
        heapq.heappush(files,temp)
        
    return count
    
files = [2, 3, 4, 5, 6, 7]
print(optimalMerge(files))
