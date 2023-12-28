### Answer 1 - Using Dijkstra’s algo and priority queue
### Time complexity - O(4*N*M), Space complexity - O(N*M+Q)~O(N*M)
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

### Answer 2 - Using Dijkstra’s algo and hashmap
### Time complexity - O(4*N*M), Space complexity - O(N*M+Q)~O(N*M)
### Intuition - given source and destination then definitely we use Dijkstras or Bellman Ford, but we don't have a negative cycle so Dijkstras, hashmap to get the speed
### and save memory for the worst case.
from collections import deque
class Solution:
    
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        queue = deque([(0, source[0], source[1])])
        distanceMap = { (source[0], source[1]) : 0 }
    
        while queue:
            distance, i, j = queue.popleft()

            if i == destination[0] and j == destination[1]:
                return distance    

            for adjI, adjJ in [ (i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1) ]:
                if adjI < 0 or adjI >= len(grid) or adjJ < 0 or adjJ >= len(grid[0]) or grid[adjI][adjJ] == 0:
                    continue
    
    
                if 1 + distance < distanceMap.get((adjI, adjJ), float('inf')):
                    distanceMap[(adjI, adjJ)] = 1 + distance
                    queue.append((1 + distance, adjI, adjJ))
    
        return -1
