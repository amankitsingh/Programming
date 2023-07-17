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
            
        return root