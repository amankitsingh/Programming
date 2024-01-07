### Answer 1 - Using Tarjan's algorithm
### Time complexity - O(V+E), Space complexity - O(V*4+Q)~O(V)
import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict
class Solution:
    def dfs(self, node, parent,adj):
        self.visited[node] = 1
        self.time[node] = self.low[node] = self.timer
        self.timer+=1
        child = 0
        for node_to in adj[node]:
            if node_to == parent:
                continue
            if self.visited[node_to] == 0:
                self.dfs(node_to, node, adj)
                self.low[node] = min(self.low[node], self.low[node_to])
                if self.low[node_to] >= self.time[node] and parent != -1:
                    self.mark[node] = 1
                child+=1
            else:
                self.low[node] = min(self.time[node_to], self.low[node])
        if child > 1 and parent==-1:
            self.mark[node] = 1
            
    
    def articulationPoints(self, n, adj):
        
        self.timer = 1
        self.visited = [0]*n
        self.mark = [0]*n
        self.time = [None]*n
        self.low = [None]*n
        self.artpoint = []
        self.dfs(0,-1, adj)
        for i in range(n):
            if self.mark[i] == 1:
                self.artpoint.append(i)
        return [-1] if len(self.artpoint) == 0 else self.artpoint
