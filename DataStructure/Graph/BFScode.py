class BFS:

	def __init__(self, n):
		self.dist = [0]*n
		self.pred = [-1]*n
		self.colors = ['white']*n
		self.graph = {0:[1], 1:[0, 2], 2: [1, 3], 
		3: [2, 4, 5], 4: [3, 5, 7], 5: [3, 4, 6, 7], 6: [5, 7], 7:[4, 5, 6]}

	def bfs(self, source):
		queue = []
		queue.append(source)
		self.dist[source] = 0
		self.colors[source] = 'Gray'
		while queue:
			current = queue.pop(0)
			print("Vertex {}".format(current))
			for i in range(len(self.graph[current])):
				if self.colors[self.graph[current][i]] == "white":
					self.colors[self.graph[current][i]] = 'Gray'

					self.dist[self.graph[current][i]] = self.dist[current] + 1
					self.pred[self.graph[current][i]] = current
					queue.append(self.graph[current][i])
			self.colors[current] = 'Black'


b = BFS(8)
b.bfs(2)

