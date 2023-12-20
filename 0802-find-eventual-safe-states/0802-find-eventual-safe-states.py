class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
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
            if pathVisited[i]==0:
                result.append(i)
        

        return sorted(result)