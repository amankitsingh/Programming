### Answer 1 - BFS
### Time complexity - O(E+N*E+N)~O(N*E), Space complexity - O(N+N+N+N+2M)~O(N+M)
from typing import List
from collections import defaultdict,deque
def shortestPath(n:int, edges: List[List[int]], src:int ) -> List[int]:
    adj = defaultdict(list)

    for node_from,node_to in edges:
        adj[node_from].append(node_to)
        adj[node_to].append(node_from)

    distance = [float("inf")]*n
    distance[src] = 0
    queue = deque()
    queue.append(src)

    while queue:
        node = queue.popleft()
        for edge in adj[node]:
            if distance[node]+1<distance[edge]:
                distance[edge] = 1 + distance[node]
                queue.append(edge)
    
    result = [-1]*n
    for i in range(n):
        if distance[i] != float("inf"):
            result[i] = distance[i]
    return result
