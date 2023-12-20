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