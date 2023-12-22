#User function Template for python3
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


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        start, end = list(map(int,input().split()))
        obj=Solution()
        print(obj.minimumMultiplications(arr, start, end))
# } Driver Code Ends