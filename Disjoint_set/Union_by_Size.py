### Disjoint set data structure
### union by size and findparent with parent compression
### TC - O(4)
class DisjointSet:
	def __init__(self, n):
		self.size = [0]*(n+1)
		self.parent = [i for i in range(n+1)]

	def findparent(self, node):
		if node == self.parent[node]:
			return node
		self.parent[node] = self.findparent[node]
		return self.parent[node]
	
	def unionbysize(self, u, v):
		ulu,ulv = self.parent[u], self.parent[v]
		if ulu == ulv:
			return
		if self.size[ulu] < self.size[ulv]:
			self.parent[ulu] = ulv
			self.size[ulv]+=self.size[ulu]
		else:
			self.parent[ulv] = ulu
			self.size[ulu]+=self.size[ulv]
