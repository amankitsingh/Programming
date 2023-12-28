#User function Template for python3

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


#{ 
 # Driver Code Starts
#Initial Template for Python 3

         
if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        source = [0] * 2
        source[0], source[1] = map(int,input().strip().split())
        destination = [0] * 2
        destination[0], destination[1] = map(int,input().strip().split())
        obj=Solution()
        print(obj.shortestPath(grid, source, destination))
# } Driver Code Ends