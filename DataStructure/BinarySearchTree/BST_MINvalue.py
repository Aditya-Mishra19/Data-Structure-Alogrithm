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

	def search(self, root, ele):
		if root is None or root.data == ele:
			return root
		if root.data > ele:
			return self.search(root.left, ele)
		return self.search(root.right, ele)

	def minValue(self, root):
		current = root
		while current.left is not None:
			current = current.left
		return current.data

	def inorder(self, root):
		if root == None:
			return
		self.inorder(root.left)
		print(root.data)
		self.inorder(root.right)



root = None
b = BST()
for ele in [10, 5, 25, 2, 7, 30]:
	root = b.buildBst(root, ele)

b.inorder(root)

search_ele = b.search(root, 7)
if search_ele == None:
	print("Element is not found")
else:
	print("Element is found in the bst{}".format(search_ele.data))










