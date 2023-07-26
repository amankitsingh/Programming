"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(rootp, level):
            nonlocal lev
            lev = max(lev, level)
            for child in rootp.children:
                dfs(child,level+1)
            return lev
        lev = 1
        return dfs(root, lev) if root else 0
