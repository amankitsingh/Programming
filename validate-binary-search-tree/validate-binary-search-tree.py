# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check_valid(root,low,high):
            if not root:
                return True
            elif not low < root.val < high:
                return False
            return check_valid(root.left, low, root.val) and check_valid(root.right, root.val, high)
        return root and check_valid(root, float("-inf"), float("inf"))