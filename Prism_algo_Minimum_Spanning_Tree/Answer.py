### Prim's Algorithm - Using min heap(priority queue)
### Time complexity - O(E*log(V)), Space complexity - O(V + Q) ~ O(V)
import heapq
from collections import defaultdict, deque
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        visited = [0]*V
        mst = 0
        pqueue = [(0,0)]
        
        while pqueue:
            weight, node = heapq.heappop(pqueue)
            if visited[node] == 0:
                visited[node] = 1
                mst += weight
                for node_to, weight in adj[node]:
                    if visited[node_to] == 0:
                        heapq.heappush(pqueue,(weight, node_to))
        return mst
