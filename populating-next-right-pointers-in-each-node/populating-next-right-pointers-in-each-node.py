"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# Answer 1 - Time complexity O(n) and space complexity O(n)
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
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
            while len(queue) > 0 and queue[0][1] == level:
                temp2,level2 = queue.popleft()
                add_neighbour(temp2,level2)
                temp.next = temp2
                temp = temp2
        return root

# Answer 2 - Time complexity O(n) and Space complexity O(1) ignoring system stack
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root and root.left:
            root.left.next = root.right
            
            if root.next:
                root.right.next = root.next.left
            
            self.connect(root.left)
            self.connect(root.right)
        return root
