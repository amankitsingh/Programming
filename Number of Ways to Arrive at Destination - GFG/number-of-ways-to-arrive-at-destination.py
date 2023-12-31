#User function Template for python3

from typing import List
from collections import defaultdict
import heapq
import sys
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        mod = 10**9+7
        for node_from,node_to,time in roads:
            adj[node_from].append((node_to, time))
            adj[node_to].append((node_from, time))
        
        src = 0
        timetaken = [float("inf")]*(n)
        timetaken[src] = 0
        ways=[0]*n
        ways[0]=1
        queue = [(0,src)]
        
        while queue:
            time, source = heapq.heappop(queue)
            if time > timetaken[source]:
                continue
            
            for node, time in adj[source]:
                new_time = time + timetaken[source]
                if new_time < timetaken[node]:
                    timetaken[node] = new_time
                    ways[node]=ways[source]
                    heapq.heappush(queue,(timetaken[node], node))
                elif new_time == timetaken[node]:
                    ways[node]=(ways[node]+ways[source])%mod
        return ways[n-1]%mod


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        adj=[]
        
        for i in range(m):
            tmp =[]
            x,y,z=map(int,input().split())
            tmp.append(x)
            tmp.append(y)
            tmp.append(z)
            adj.append(tmp)
            
        
        
        
       
        obj = Solution()
        res = obj.countPaths(n, adj)
        
        print(res)
        

# } Driver Code Ends