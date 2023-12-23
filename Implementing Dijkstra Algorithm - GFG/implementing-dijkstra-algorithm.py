from collections import deque
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        distance = [float("inf")]*V
        distance[S] = 0
        queue = deque()
        queue.append((S,0))
        
        while queue:
            node,dist = queue.popleft()
            for edges in adj[node]:
                node_to = edges[0]
                weight = edges[1]
                if dist+weight < distance[node_to]:
                    if distance[node_to]!= float("inf"):
                        if (node_to, distance[node_to]) in queue:
                            queue.remove((node_to, distance[node_to]))
                        
                    distance[node_to] = dist+weight
                    queue.append((node_to,distance[node_to]))
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