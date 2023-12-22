### Answer 1 - using BFS and graph traversal
### Time complexity - O(mod*N), Space complexity - O(mod*N)
from typing import List
from collections import deque
class Solution:
    
    def minimumMultiplications(self, a : List[int], start : int, end : int) -> int:
        if start == end:
            return 0
    
        mod = 100000
        queue = deque()
        queue.append((start,0))
        distance = [float("inf")]*mod
        distance[start]=0
    
        while queue:
            points, steps = queue.popleft()
            for i in a:
                multiple = (points*i)%mod
                if steps+1<distance[multiple]:
                    distance[multiple] = steps+1
                    if multiple == end:
                        return steps+1
                    queue.append((multiple, steps+1))
    
        return -1
