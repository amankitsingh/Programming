### Disjoint datastructure to get the minimum spannig tree of the tree
### for large cases unionbysize is good, unionbyrank will fail 
### Time complexity - O(V+E + nlogn + n)~O(nlogn), Space complexity - O(V+V+E)~O(V)
class DSU:
    def __init__(self, n):
        self.size = [0]*(n)
        self.rank = self.size[:]
        self.parent = [i for i in range(n)]
    
    def findParent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    
    def unionbysize(self, u, v):
        ulp_u = self.parent[u]
        ulp_v = self.parent[v]
        if ulp_u == ulp_v:
            return
        elif self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v]+=self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u]+=self.size[ulp_v]

    def unionbyrank(self, u, v):
        ulp_u = self.parent[u]
        ulp_v = self.parent[v]
        if ulp_u == ulp_v:
            return
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v]+=1
            
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        dsu = DSU(V+1)
        edges = []
        for i in range(V):
            for node_to, wt in adj[i]:
                edges.append([i,node_to,wt])
        
        edges.sort(key=lambda x:x[2])
        
        mst = 0
        for u,v,wt in edges:
            if dsu.findParent(u) != dsu.findParent(v):
                mst+=wt
                dsu.unionbysize(u,v)
        return mst
