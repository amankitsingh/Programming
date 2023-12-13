### Answer 1 - DFS
### Time complexity - O(N*N), Space complexity - O(N)+O(N)+O(N)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        taken = set()

        for node_from,node_to in prerequisites:
            adj[node_from].append(node_to)
    
        def dfs(node):
            if not adj[node]:
                return True
            if node in taken:
                return False
            taken.add(node)
            for it in adj[node]:
                if not dfs(it):
                    return False
            adj[node] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        else:
            return True
