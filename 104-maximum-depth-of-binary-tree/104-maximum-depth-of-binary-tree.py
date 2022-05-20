# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfh(root, level=0):
            if root is None:
                return level
            return max(dfh(root.left,level+1),dfh(root.right,level+1))
        return dfh(root)