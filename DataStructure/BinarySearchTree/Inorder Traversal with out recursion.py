#Inorder Traversal with out recursion 

class Node:

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class BST:

	def buildBst(self, root, ele):
		if root == None:
			return Node(ele)
		if ele < root.data:
			root.left = self.buildBst(root.left, ele)
		else:
			root.right = self.buildBst(root.right, ele)
		return root

	def inorder(self, root):
		#set current to root of binary search tree
		current = root
		stack = []

		while True:
			# reach the left most node of the current root
			if current is not None:
				stack.append(current)
				current = current.left
			elif stack:
				current = stack.pop()
				print(current.data)
				current = current.right
			else:
				break


root = None
b = BST()
for ele in [10, 5, 25, 2, 7, 30]:
	root = b.buildBst(root, ele)
b.inorder(root)

