### DFS approach
### cane also be solved in reverse kahn's algo approach
### Time complexity - O(V*E), Space complexity - O(2V+V)~O(V)
class Solution:    
    def eventualSafeNodes(self, V : int, graph : List[List[int]]) -> List[int]:
        n = len(graph)
        result = []
        visited = [0]*n
        pathVisited = visited[:]
        
        def dfs(node):
            if pathVisited[node] == 1:
                return True
            if visited[node]:
                return False
            
            pathVisited[node] = 1
            visited[node] = 1
            for edge in graph[node]:
                if dfs(edge):
                    return True
            pathVisited[node] = 0
            return False

        for i in range(n):
            if visited[i] == 0:
                dfs(i)
        
        for i in range(n):
            if pathVisited[i] == 0:
                result.append(i)


        return sorted(result)
