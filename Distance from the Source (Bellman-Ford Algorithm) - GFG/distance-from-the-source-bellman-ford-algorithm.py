### Bellman Ford algorithm
### Time complexity - O(V*E + E) ~ O(V*E), Space complexity - O(V)
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
