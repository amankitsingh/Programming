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
