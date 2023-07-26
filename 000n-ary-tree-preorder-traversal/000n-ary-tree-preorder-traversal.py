"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def preorder(root):
            if not root:
                return
            result.append(root.val)
            for child in root.children:
                preorder(child)
        result = []
        children(root)
        return result
