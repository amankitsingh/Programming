### Disjoint set data structure
### union by rank and findparent with parent compression
### TC -  O(4)
class DisjoinSet:
	def __init__(self, n):
		self.rank = [0]*n
		self.parent = [i for i in range(n)]

	def findparent(self, node):
		if node == self.parent[node]:
			return node
		self.parent[node] = self.findparent[node]
		return self.parent[node]
	
	def unionbyrank(self, u, v):
		upu,upv = self.parent[u], self.parent[v]
		if upu == upv:
			return
		if self.rank[ulu] < self.rank[ulv]:
			self.parent[ulu] = ulv
		elif self.rank[ulv] < self.rank[ulu]:
			self.parent[ulv] = ulu
		else:
			self.parent[ulv] = ulu
			self.rank[ulu]+=1
