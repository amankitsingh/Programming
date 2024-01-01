from typing import List
import heapq
from collections import defaultdict,deque
class Solution:
    def CheapestFLight(self,n,flights,src,dst,k):
        adj = defaultdict(list)
        
        for node_from,node_to, weight  in flights:
            adj[node_from].append((node_to,weight))
            
        distance = [[float("inf")]*(k+2) for _ in range(n)]
    
        queue = [[0,k+1,src]]
        
        while queue:
            dist, stepsLeft, node = heapq.heappop(queue)
            if node == dst:
                return dist
            if stepsLeft > 0:
                for node_to, weight in adj[node]:
                    new_dist = dist + weight
                    if new_dist < distance[node_to][stepsLeft-1]:
                        distance[node_to][stepsLeft-1] = new_dist
                        heapq.heappush(queue, (new_dist, stepsLeft-1,node_to))                
                
        return -1
