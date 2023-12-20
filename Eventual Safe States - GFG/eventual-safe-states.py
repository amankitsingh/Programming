#User function Template for python3

from typing import List

class Solution:    
    def eventualSafeNodes(self, V : int, graph : List[List[int]]) -> List[int]:
        n = len(graph)
        result = []
        visited = [0]*n
        pathVisited = visited[:]
        
        def dfs(node):
            if pathVisited[node] == 1:
                return True
            if visited[node]:
                return False
            
            pathVisited[node] = 1
            visited[node] = 1
            for edge in graph[node]:
                if dfs(edge):
                    return True
            pathVisited[node] = 0
            return False

        for i in range(n):
            if visited[i] == 0:
                dfs(i)
        
        for i in range(n):
            if pathVisited[i] == 0:
                result.append(i)


        return sorted(result)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
        obj = Solution()
        ans = obj.eventualSafeNodes(V, adj)
        for nodes in ans:
            print(nodes, end = ' ')
        print()
            


# } Driver Code Ends