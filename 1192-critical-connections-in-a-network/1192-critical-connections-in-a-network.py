### Answer 1 - Using Tarjan's algo
### Time complexity - O(V+2E), Space complexity - O(V+2E + 3V))~O(V+2E)
from collections import defaultdict
class Solution:
    def dfs(self, node, parent):
        self.visited[node] = 1
        self.time[node] = self.low[node] = self.timer
        self.timer+=1
        for node_to in self.adj[node]:
            if node_to == parent:
                continue
            if self.visited[node_to] == 0:
                self.dfs(node_to, node)
                # take the lowest of all the adjacent nodes
                self.low[node] = min(self.low[node_to], self.low[node])
                #check if a bridge can be made
                if self.low[node_to] > self.time[node]:
                    self.bridges.append([node,node_to])
            else:
                # you have visited it, no bridge possible, just take the minium lowest time of insertion
                self.low[node] = min(self.low[node], self.low[node_to])
                
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.adj = defaultdict(list)
        for node_from, node_to in connections:
            self.adj[node_from].append(node_to)
            self.adj[node_to].append(node_from)
        
        self.timer = 1
        self.visited = [0]*n
        self.time = [None]*n
        self.low = [None]*n
        self.bridges = []
        self.dfs(0,-1)
        return self.bridges
