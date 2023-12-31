### Answer 1 - Usign dijkstra's and min heap(priority queue)
### Time complexity - O(V*Elog(V)), Space complexity - O(adj + 2*V + Q)~O(adj)
import heapq
from collections import defaultdict
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        mod = 1_000_000_007
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
