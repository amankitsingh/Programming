class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        nodes_colored = [-1]*n

        def dfs(node, color):
            nodes_colored[node] = color
            new_color = 1 if color == 0 else 0
            for adj in graph[node]:
                if nodes_colored[adj]==-1:
                    if dfs(adj,new_color) == False:
                        return False
                else:
                    if nodes_colored[adj] == color:
                        return False
            return True
        for i in range(n):
            if nodes_colored[i]==-1:
                if dfs(i, 0) == False:
                    return False
        return True
