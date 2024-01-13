class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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

        return result[::-1] if len(result) == numCourses else []