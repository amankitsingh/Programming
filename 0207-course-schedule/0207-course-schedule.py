### Answer 1 - DFS
### Time complexity - O(N*N), Space complexity - O(N)+O(N)+O(N)~O(N)
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

### Answer 2 - Using Kahn's algorithm - BFS
### Time complexity - O(V+E), Space complexity - O(N)+O(N)+O(N) ~O(N)
### Better solution
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        queue = deque()
        indegree = [0]*(numCourses+1)
        result = []

        for cou_from, cou_to in prerequisites:
            adj[cou_from].append(cou_to)
            indegree[cou_to]+=1


        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            result.append(node)
            for it in adj[node]:
                indegree[it]-=1
                if indegree[it] == 0:
                    queue.append(it)

        return len(result) == numCourses
