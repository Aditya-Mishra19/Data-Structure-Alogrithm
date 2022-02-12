class Kruskal:

	def __init__(self, n):
		self.V = n
		self.graph = []

	def add_edge(self, u, v, w):
		self.graph.append([u, v, w])

	def find(self, parent, i):
		if parent[i] == i:
			return i 
		return self.find(parent, parent[i])

	def krusals_algo(self):
		result = []
		self.graph = sorted(self.graph, key=lambda item: item[2])
		parent = [k for k in range(self.V)]

		i, e = 0, 0
		while e < self.V - 1:
			u, v, w = self.graph[i]
			x = self.find(parent, u)
			y = self.find(parent, v)
			if x != y:
				result.append([u, v, w])
				parent[y] = x 
				e += 1
			i += 1
		print(result)

g = Kruskal(6)
g.add_edge(0, 1, 4)
g.add_edge(1, 0, 4)
g.add_edge(0, 2, 4)
g.add_edge(2, 0, 4)
g.add_edge(1, 2, 2)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 3)
g.add_edge(3, 2, 3)
g.add_edge(2, 5, 2)
g.add_edge(5, 2, 2)
g.add_edge(2, 4, 4)
g.add_edge(4, 2, 4)
g.add_edge(3, 4, 3)
g.add_edge(4, 3, 3)
g.add_edge(4, 5, 3)
g.add_edge(5, 4, 3)
g.krusals_algo()
