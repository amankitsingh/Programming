#User function Template for python3
from collections import defaultdict,deque
class Solution:
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        mod = 100000000
        distance = [mod]*V
        distance[S] = 0
        
        for i in range(V-1):
            for i in edges:
                node_from = i[0]
                node_to = i[1]
                weight = i[2]
                if distance[node_from]!= mod and distance[node_from]+weight<distance[node_to]:
                    distance[node_to] = distance[node_from]+weight
        
        
        for i in edges:
            node_from = i[0]
            node_to = i[1]
            weight = i[2]
            if distance[node_from]!= mod and distance[node_from]+weight<distance[node_to]:
                return [-1]
    
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
        edges = []
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            edges.append([u,v,w])
        S=int(input())
        ob = Solution()
        
        res = ob.bellman_ford(V,edges,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends