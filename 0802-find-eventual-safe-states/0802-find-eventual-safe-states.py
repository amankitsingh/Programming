### Answer 1 - BFS - reverse kahn's algorithm
### Time complexity - O(V*E), Space complexity - O(V+Q) ~ O(V)
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        queue = deque()
        V = len(graph)
        indegree = [0]*V
    
        graphrev = defaultdict(list)
        for node in range(V):
            for v in graph[node]:
                graphrev[v].append(node)
                indegree[node]+=1
    
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
    
        result = []
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            for node in graphrev[vertex]:
                indegree[node]-=1
                if indegree[node] == 0:
                    queue.append(node)
                    
        return sorted(result)

### Answer 2 - DFS
### Time complexity - O(V*E), Space complexity - O(2*V + V)~O(V) auxiliary stack and visited and pathVisited array
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
