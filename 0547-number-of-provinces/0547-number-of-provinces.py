### Answer 1 - DFS approach
### Time complexity - O(N)+O(2E), Space complexity - O(N) +O(S)
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [0]*len(isConnected[0])
        def dfs(node, visited):
            for i in range(len(isConnected[0])):
                if isConnected[node][i] ==1:
                    isConnected[node][i] = -1
                    if visited[i]==0:
                        visited[i]=1
                        dfs(i,visited)
            return 1
        result = 0
        for i in range(len(isConnected[0])):
            if visited[i]==0:
                result+=dfs(i, visited)
        return result

### Answer 2
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [0]*len(isConnected[0])
        def dfs(node, visited):
            visited[node]=1
            for i in range(len(isConnected[0])):
                if isConnected[node][i] ==1 and visited[i]==0:
                    dfs(i,visited)
        result=0
        for i in range(len(isConnected[0])):
            if visited[i]==0:
                result+=1
                dfs(i, visited)
        return result
