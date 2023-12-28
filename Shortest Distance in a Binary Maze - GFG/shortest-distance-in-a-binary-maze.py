### Answer 1 - Using Dijkstra’s algo and priority queue
### Time complexity - O(E*log(V), Space complexity - O(N*M+Q)~O(N*M)
### Intuition - given source and destination then definitely we use Dijkstras or bellman ford, but we don't have a negative cycle so Dijkstras, priority queue to get the speed
### else normal queue will also work
from typing import List
from collections import deque
import heapq
class Solution:
    
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        if source == destination:
            return 0
        n = len(grid)
        m = len(grid[0])
        destdistance = [[float("inf")]*m for _ in range(n)]
        queue = [[0,source[0],source[1]]]
        
        while queue:
            steps,x,y = heapq.heappop(queue)
            directions = [0,1,0,-1,0]
            for k in range(len(directions)-1):
                dx,dy = x + directions[k], y + directions[k+1]
                if 0<= dx < n and 0<= dy < m and grid[dx][dy] == 1 and steps+1 < destdistance[dx][dy]:
                    destdistance[dx][dy] = steps + 1
                    if [dx,dy] == destination:
                        return destdistance[dx][dy]
                    heapq.heappush(queue,(steps+1, dx,dy))
        
        return -1
