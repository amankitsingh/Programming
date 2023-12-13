### Answer 1 - usign DFS
### Time complexity - O(N*2E) + O(N), Space complexity - O(N)+O(N)
def cycleDetection(edges, n, m):
    adj = [[] for _ in range(n+1)]
    if m == 0:
        return "No"
    visited = [0]*(n+1)

    for node_from,node_to in edges:
        adj[node_from].append(node_to)
        adj[node_to].append(node_from)

    def dfs(node, parent):
        visited[node] = 1
        for it in adj[node]:
            if visited[it] == 0:
                if dfs(it, node) == "Yes":
                    return "Yes"
            elif it!=parent:
                return "Yes"
        return "No"
    for i in range(1,n+1):
        if visited[i] == 0:
            if dfs(i, i) == "Yes":
                return "Yes"
    else:
        return "No"

### Answer  - usign BFS
### Time complexity - O(N*2E) + O(N), Space complexity - O(N)+O(N)
from collections import deque
def cycleDetection(edges, n, m):
    adj = [[] for _ in range(n+1)]
    if m == 0:
        return "No"
    visited = [0]*(n+1)

    for node_from,node_to in edges:
        adj[node_from].append(node_to)
        adj[node_to].append(node_from)

    def bfs(node, parent):
        visited[node] = 1
        queue = deque()
        queue.append([node,parent])
        while queue:
            start,parent = queue.popleft()
            for edge in adj[start]:
                if visited[edge] == 0:
                    visited[edge] = 1
                    queue.append([edge,start])
                elif parent != edge:
                    return "Yes"
        return "No"
    for i in range(1,n+1):
        if visited[i] == 0:
            if bfs(i, -1) == "Yes":
                return "Yes"
    else:
        return "No"
