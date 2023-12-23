from collections import deque
import heapq
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        distance = [float("inf")]*V
        distance[S] = 0
        pq = [(S,0)]
        
        while pq:
            node,dist = heapq.heappop(pq)
            if dist > distance[node]:
                continue
            for node_to,weight in adj[node]:
                new_dist = dist + weight
                if new_dist < distance[node_to]:
                    distance[node_to] = new_dist
                    heapq.heappush(pq,(node_to,new_dist))
        return distance

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends