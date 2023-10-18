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