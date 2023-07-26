"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        def ppostorder(root):
            if not root:
                return
            for child in root.children:
                ppostorder(child)
            result.append(root.val)
        ppostorder(root)
        return result