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

	def preorder(self, root):
		if root is None:   # if not root
			return
		print(root.data)
		self.preorder(root.left)
		self.preorder(root.right)

	def iterativePreorder(self, root):
		if root is None:
			return
		stack = []
		stack.append(root)
		while stack:
			current = stack.pop()
			print(current.data)

			if current.right:
				stack.append(current.right)
			if current.left:
				stack.append(current.left)

root = None
b = BST()
for ele in [10, 5, 25, 2, 7, 30]:
	root = b.buildBst(root, ele)

b.preorder(root)
print("***")
b.iterativePreorder(root)
