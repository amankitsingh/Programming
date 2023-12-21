### Answer 1 - Using Kahn's algorithm 
### Time complexity - O(N*M + K + K + Q) ~ O(N*M), Space complexity - O(K + N + N)~O(N)
### Here M is the length of the largest word in the array, Q is the queue
### Intuition
### to check all the consecutive pairs of the words and find the differentiating factor and map them as a graph, to get the problem down to topological sort.
from collections import defaultdict,deque
class Solution:
    def findOrder(self,alien_dict, N, K):
        topo = defaultdict(list)
        indegree = [0]*K
        for i in range(N-1):
            for j in range(min(len(alien_dict[i]),len(alien_dict[i+1]))):
                if alien_dict[i][j]!=alien_dict[i+1][j]:
                    topo[ord(alien_dict[i][j])-97].append(ord(alien_dict[i+1][j])-97)
                    break
        
        for i in range(K):
            for j in topo[i]:
                indegree[j]+=1
                
        queue = deque()
    
        for i in range(K):
            if indegree[i] == 0:
                queue.append(i)
        
        result = []
    
        while queue:
            character = queue.popleft()
            result.append(chr(97+character))
            for adj_node in topo[character]:
                indegree[adj_node]-=1
                if indegree[adj_node] == 0:
                    queue.append(adj_node)
        
        return result
