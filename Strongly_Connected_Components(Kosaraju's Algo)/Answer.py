### Answer 1 - Kosaraju algo to find the strongly connected components
### Time complexity - o(3*V*E)~O(V*E), Space complexity - O(V+S+V*E)~O(V*E)
### Intuition - if we reverse the edges then the connected component remains same, because u->v or v->u will stay connect
### First make the stack concerning start and finish time, meaning FIFO
### then reverse the edges 
### then iterate the stack and loop through the nodes and repeat the process till stack is empty
from collections import defaultdict
class Solution:
    
    def dfs(self, node, adj):
        self.visited[node] = 1
        for node_to in adj[node]:
            if self.visited[node_to] == 0:
                self.dfs(node_to, adj)
        self.finish_stack.append(node)
    
    def get_scc(self, node):
        self.visited[node] = 1
        for node_to in self.revadj[node]:
            if self.visited[node_to]==0:
                self.get_scc(node_to)
    
    def kosaraju(self, V, adj):
        self.visited = [0]*V
        self.finish_stack = []
        
        # get the sorted edges
        for node in range(V):
            if self.visited[node] == 0:
                self.dfs(node, adj)
        
        # reverse the graph
        self.revadj = defaultdict(list)
        for i in range(V):
            self.visited[i] = 0
            for node_to in adj[i]:
                self.revadj[node_to].append(i)
        
        self.result = 0
        # do dfs to get result
        while self.finish_stack:
            node_from = self.finish_stack.pop()
            if self.visited[node_from] == 0:
                self.result+=1
                self.get_scc(node_from)
                
        return self.result
