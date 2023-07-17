"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# Answer 1 - Time complexity O(n) and Space Complexity O(n)
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
            while len(queue) > 0 and queue[0][1] == level:
                temp2,level2 = queue.popleft()
                add_neighbour(temp2,level2)
                temp.next = temp2
                temp = temp2
        return root

# Answer 2 - Time Complexity O(n) and Space Complexity O(1)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root and root.left and root.right:
            root.left.next = root.right
            if root.right:
                temp = root.next
                while temp and temp.next and (temp.left is None and temp.right is None):
                    temp=temp.next
                if temp:
                    root.right.next = temp.left or temp.right
        else:
            if root and root.next and (root.left or root.right):
                if root.left:
                    temp = root.next
                    while temp.next and (temp.left is None and temp.right is None):
                        temp=temp.next
                    if temp.left:
                        root.left.next = temp.left
                    elif temp.right:
                        root.left.next = temp.right
                else:
                    temp = root.next
                    while temp.next and (temp.left is None and temp.right is None):
                        temp=temp.next
                    if temp.left:
                        root.right.next = temp.left
                    elif temp.right:
                        root.right.next = temp.right
        if root:
            self.connect(root.right)
            self.connect(root.left)
        return rootclass Solution:

# Answer 3 - Time Complexity O(n) and Space Complexity O(1)
def connect(self, root: 'Node') -> 'Node':
    if root is None:
        return
    scanner = root.next
    while scanner:
        if scanner.left:
            scanner = scanner.left
            break
        elif scanner.right:
            scanner = scanner.right
            break
        scanner = scanner.next
    if root.right:
        root.right.next = scanner
    if root.left:
        root.left.next = root.right if root.right else scanner
    self.connect(root.right)
    self.connect(root.left)
    return root
