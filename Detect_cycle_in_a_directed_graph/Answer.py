### Answer 1
### Time complexity - o(V+V*E), Space complexity - O(V+V)~O(V)
from collections import defaultdict
def isCyclic(edges, v, e):
    adj = defaultdict(list)
    for ver,edge in edges:
        adj[ver].append(edge)
        
    visited = [-1]*(v+1)
    path_visited = visited[:]

    def dfs(node):
        visited[node] = 1
        path_visited[node] = 1
        for j in adj[node]:
            if visited[j] == -1:
                if dfs(j):
                    return True
            elif path_visited[j] == 1:
                return True
        path_visited[node] = 0
        return False
    for i in range(v):
        if visited[i] == -1:
            if dfs(i):
                return True
    return False
