### Answer 1 - Implementation using deque
### Time complexity - O(V*E+Q), Space complexity - O(V)
from collections import deque
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        distance = [float("inf")]*V
        distance[S] = 0
        queue = deque()
        queue.append((S,0))
        
        while queue:
            node,dist = queue.popleft()
            for edges in adj[node]:
                node_to = edges[0]
                weight = edges[1]
                if dist+weight < distance[node_to]:
                    if distance[node_to]!= float("inf"):
                        if (node_to, distance[node_to]) in queue:
                            queue.remove((node_to, distance[node_to]))
                        
                    distance[node_to] = dist+weight
                    queue.append((node_to,distance[node_to]))
        return distance
        
### Answer 2 - Implementation using min-heap (priority queue) to reduce the time complexity
### Time complexity - O(V*E), Space complexity - O(V)
import heapq
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        distance = [float("inf")]*V
        distance[S] = 0
        pq = [(S,0)]
        
        while pq:
            node,dist = heapq.heappop(pq)
            if dist > distance[node]:
                continue
            for node_to,weight in adj[node]:
                new_dist = dist + weight
                if new_dist < distance[node_to]:
                    distance[node_to] = new_dist
                    heapq.heappush(pq,(node_to,new_dist))
        return distance
