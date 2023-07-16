# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def f(root,s):
            if not root: return False
            if not root.left and not root.right: return root.val == s
            return f(root.left,s-root.val) or f(root.right,s-root.val)
        return f(root,targetSum) if root else False