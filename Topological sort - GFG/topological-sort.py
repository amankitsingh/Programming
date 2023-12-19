### Answer 1 - DFS
### Time complexity - O(V*E), Space complexity - O(2V)~O(V)
class Solution:
    def topoSort(self, V, adj):
        result = []
        visited = [0]*V
    
        def dfs(node):
            visited[node] = 1
            for adjnod in adj[node]:
                if visited[adjnod] == 0:
                    dfs(adjnod)
            result.append(node)
        
        for i in range(V):
            if visited[i]==0:            
                dfs(i)
                
        return result[::-1]


### Answer 2 - BFS = kahn's algorithm
### Time complexity - O(V+V+V*E)~O(V*E), Space complexity - O(2*V)~O(V)
from collections import deque
class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        queue = deque()
        indegree = [0]*V
    
        for node in range(V):
            for v in adj[node]:
                indegree[v]+=1
    
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
    
        result = []
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            for node in adj[vertex]:
                indegree[node]-=1
                if indegree[node] == 0:
                    queue.append(node)
        return result
