class Node:

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class ExpressionTree:
	def evaluate(self, root):
		if root is None:
			return 0
		if root.left == None and root.right == None:
			return int(root.data)

		left = self.evaluate(root.left)
		right = self.evaluate(root.right)
		if root.data == '+':
			return left + right
		elif root.data == '*':
			return left * right
		elif root.data == '-':
			return left - right 
		elif root.data == '/':
			return left /right
		elif root.data == '^':
			return left ** right


root = Node('*')
root.left = Node('+')
root.right = Node('*')
root.left.left = Node('2')
root.left.right = Node('3')
root.right.left = Node('4')
root.right.right = Node('+')
root.right.right.left = Node('5')
root.right.right.right = Node('6')
e = ExpressionTree()
result = e.evaluate(root)
print(result)



