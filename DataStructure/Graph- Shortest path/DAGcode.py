from collections import defaultdict
class Graph:
    def __init__(self,n):
        self.V=n
        self.graph=defaultdict(list)
        
    def addEdge(self,u,v,w):
        self.graph[u].append((v,w))
        
    def topological_helper(self,v,visited,stack):
        visited[v]=True
        for i in range(self.V):
            if visited[i] == False:
                self.topological_helper(i,visited,stack)
        self.stack.append(v)
        
    def relax(self,u,v,w):
        if self.distance[v]>self.distance[u]+w:
            self.distance[v]=self.distance[u]+w
        
    def topological(self):
        self.stack=[]
        visited=[False]*self.V
        for i in range(self.V):
            if visited[i]==False:
                self.topological_helper(i,visited,self.stack)
                
    def DAG(self,src):
        self.topological()
        print(self.stack)
        self.distance=[99999]*self.V
        self.distance[src]=0
        while self.stack:
            i=self.stack.pop()
            for v,w in self.graph[i]:
                self.relax(i,v,w)
                
    def print_edge(self):
        for i in range(self.V):
            print(self.distance[i])
g = Graph(6) 
g.addEdge(0, 1, 5) 
g.addEdge(0, 2, 3) 
g.addEdge(1, 3, 6) 
g.addEdge(1, 2, 2) 
g.addEdge(2, 4, 4) 
g.addEdge(2, 5, 2) 
g.addEdge(2, 3, 7) 
g.addEdge(3, 4, -1) 
g.addEdge(4, 5, -2) 


s = 1
g.DAG(s)
g.print_edge()

       
    
