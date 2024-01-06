### Answer 1 - Using Disjoint Set
### Time complexity - O(N+E*4*aplha)~O(N), Space complexity - O(N*2 + N + N)~O(N)
class DisjointSet:
    def __init__(self, size):
        self.size = [1]*size
        self.parent = list(range(size))
    
    def findparent(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.findparent(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        ulp_u,ulp_v = self.findparent(u), self.findparent(v)
        if ulp_v == ulp_u:
            return 0
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v]+=self.size[ulp_u]
        else:
            self.parent[ulp_v]= ulp_u
            self.size[ulp_u]+=self.size[ulp_v]
        return 1
    # Another way of writing    
    def union(self, u, v):
        ulp_u,ulp_v = self.findparent(u), self.findparent(v)
        if ulp_v == ulp_u:
            return 0
        if self.size[ulp_u] < self.size[ulp_v]:
            ulp_u, ulp_v = ulp_v, ulp_u
        self.parent[ulp_v] = self.parent[ulp_u]
        self.size[ulp_u]+=self.size[ulp_v]
        return 1
    
            
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        dsu = DisjointSet(n)
        rows, cols = {}, {}
        removed = 0
        for i, (row, col) in enumerate(stones):
            if row in rows:
                removed += dsu.union(i, rows[row])
            else:
                rows[row] = i
            if col in cols:
                removed += dsu.union(i, cols[col])
            else:
                cols[col] = i
        
        return removed
                
