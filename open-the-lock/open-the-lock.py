class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def possible_outcomes(nodes):
            extend_queue = []
            for i,value in enumerate(node):
                number = int(value)
                extend_queue.append(node[:i] + str((number - 1) % 10) + node[i+1:])
                extend_queue.append(node[:i] + str((number + 1) % 10) + nodes[i+1:])
            return extend_queue
        depth, visited, queue = -1, set(deadends), collections.deque(["0000"])
        
        while queue:
            depth += 1
            for i in range(len(queue)):
                node = queue.popleft()
                if node == target:
                    return depth
                if node in visited:
                    continue
                visited.add(node)
                queue.extend(possible_outcomes(node))
        return -1