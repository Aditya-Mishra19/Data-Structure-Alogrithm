class Converstion:

	def __init__(self):
		self.stack = []
		self.result = []
		self.precedence = {'(': 0, '+': 1, '-': 1,
		'*': 2, '/': 2, '^': 3}

	def push(self, c):
		self.stack.append(c)

	def isEmpty(self):
		return self.stack == []

	def peek(self):
		if not self.isEmpty():
			return self.stack[-1]
		else:
			return '$'

	def pop(self):
		if not self.isEmpty():
			return self.stack.pop()
		else:
			return '$'

	def notGreater(self, c):
		try:
			a = self.precedence[self.peek()]
			b = self.precedence[c]

			return True if a >= b else False
		except KeyError:
			return False


	def infixToPostfix(self, exp):

		for c in exp:
			if c.isalnum():
				self.result.append(c)
			elif c == '(':
				self.push(c)
			elif c == ')':
				x = self.pop()
				while x != '(':
					self.result.append(x)
					x = self.pop()
			else:
				while (not self.isEmpty() and self.notGreater(c)):
					self.result.append(self.pop())
				self.push(c)

		while not self.isEmpty():
			self.result.append(self.pop())

		return "".join(self.result)

c = Converstion()
result = c.infixToPostfix("(2*3+4*(5-6))")
print(result)
