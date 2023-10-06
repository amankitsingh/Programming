"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def add_neighbour(te, lev):
            if te.left:
                queue.append([te.left, lev+1])
            if te.right:
                queue.append([te.right, lev+1])
        queue = deque()
        if root is None:
            return
        queue.append((root,0))
        while queue:
            temp,level = queue.popleft()
            add_neighbour(temp,level)
            if len(queue) > 0 and queue[0][1] == level:
                temp.next = queue[0][0]
        return root