### Answer 1 - Using Disjoint Set of union of size
### Time complexity - O(E*4*aplha + N)~O(E), Space complexity - O(N+N)~O(N)
class DisjointSet:
    def __init__(self, size):
        self.size =[0]*(size)
        self.parent = [i for i in range(size)]
        
    def findparent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findparent(self.parent[node])
        return self.parent[node]
    def unionbysize(self, u, v):
        ulp_u = self.parent[u]
        ulp_v = self.parent[v]
        if ulp_u == ulp_v:
            return 
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v]+=self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]
            
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        dsu = DisjointSet(n)
        cntremoveedge = 0
        for node_from, node_to in connections:
            if dsu.findparent(node_from) == dsu.findparent(node_to):
                cntremoveedge+=1
            else:
                dsu.unionbysize(node_from, node_to)
        cntedgeneeded = 0
        for node,node_parent in enumerate(dsu.parent):
            if node==node_parent:
                cntedgeneeded+=1
        ans = cntedgeneeded-1
        return ans if cntremoveedge >= ans else -1
