"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def children(root):
            if not root:
                return
            result.append(root.val)
            for child in root.children:
                children(child)
        result = []
        children(root)
        return result