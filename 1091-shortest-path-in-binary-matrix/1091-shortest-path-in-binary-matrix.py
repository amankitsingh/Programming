### up,down,left,right = [0,1,0,-1,0]
### diagonal up,left,down,right = [-1,-1,1,1,-1]
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        source = [0,0]
        destination = [n-1,n-1]
        if grid[source[0]][source[1]] == 1:
            return -1
        if source == destination:
            return 1
        destdistance = [[float("inf")]*n for _ in range(n)]
        checker = 0
        queue = [[1,source[0],source[1]]]
        
        while queue:
            steps,x,y = heapq.heappop(queue)
            if [x,y] == destination:
                return steps
            directions = [0,1,0,-1,0]
            for k in range(len(directions)-1):
                dx,dy = x + directions[k], y + directions[k+1]
                if 0<= dx < n and 0<= dy < n and grid[dx][dy] == checker and steps+1 < destdistance[dx][dy]:
                    destdistance[dx][dy] = steps + 1
                    heapq.heappush(queue,(steps+1, dx,dy))
            diagonaldirections = [-1,-1,1,1,-1]
            for k in range(len(diagonaldirections)-1):
                dx,dy = x + diagonaldirections[k], y + diagonaldirections[k+1]
                if 0<= dx < n and 0<= dy < n and grid[dx][dy] == checker and steps+1 < destdistance[dx][dy]:
                    destdistance[dx][dy] = steps + 1
                    heapq.heappush(queue,(steps+1, dx,dy))
        
        return -1
