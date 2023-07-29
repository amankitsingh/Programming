# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balance(root):
            if not root:
                return True, 0
            left_balance, left_val = balance(root.left)
            right_balance, right_val = balance(root.right)
            balanced = left_balance and right_balance and abs(left_val-right_val) <= 1
            return balanced, 1+max(left_val,right_val)
        return balance(root)[0]