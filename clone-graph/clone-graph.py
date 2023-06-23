"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        memo = {}
        def clone(node):
            if node not in memo:
                temp_node = memo[node] = Node(node.val, [])
                temp_node.neighbors = list(map(clone, node.neighbors))
            return memo[node]
        return node and clone(node)
            