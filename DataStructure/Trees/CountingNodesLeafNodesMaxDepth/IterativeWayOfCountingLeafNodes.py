# Python3 program to count leaf nodes 
# in a Binary Tree 
from queue import Queue 

# Helper function that allocates a new 
# Node with the given data and None 
# left and right pointers. 
class newNode: 
	def __init__(self, data): 
		self.data = data 
		self.left = self.right = None
		
# Function to get the count of leaf 
# Nodes in a binary tree 
def getLeafCount(node): 
	
	# If tree is empty 
	if (not node): 
		return 0

	# Initialize empty queue. 
	q = Queue() 

	# Do level order traversal 
	# starting from root 
	count = 0 # Initialize count of leaves 
	q.put(node) 
	while (not q.empty()): 
		temp = q.queue[0] 
		q.get() 

		if (temp.left != None): 
			q.put(temp.left) 
		if (temp.right != None): 
			q.put(temp.right) 
		if (temp.left == None and
			temp.right == None): 
			count += 1
	return count 

# Driver Code 
if __name__ == '__main__': 
	
	# 1 
	# / \ 
	# 2 3 
	# / \ 
	# 4 5 
	# Let us create Binary Tree shown 
	# in above example 
	root = newNode(1) 
	root.left = newNode(2) 
	root.right = newNode(3) 
	root.left.left = newNode(4) 
	root.left.right = newNode(5) 

	# get leaf count of the above 
	# created tree 
	print(getLeafCount(root)) 

# This code is contributed by PranchalK 

