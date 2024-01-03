### Disjoint set data structure
### union by size and findparent with parent compression
class DisjoinSet:
	def __init__(self, n):
		self.rank = [0]*n
		self.parent = [i for i in range(n)]

	def findparent(self, node):
		if node == self.parent[node]:
			return node
		self.parent[node] = self.findparent[node]
		return self.parent[node]
	
	def unionbysize(self, u, v):
		upu,upv = self.parent[u], self.parent[v]
		if upu == upv:
			return
		if self.size[ulu] < self.size[ulv]:
			self.parent[ulu] = ulv
			self.size[ulv]+=self.size[ulu]
		else:
			self.parent[ulv] = ulu
			self.size[ulu]+=self.size[ulv]
