# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        answer = []
        def dfs(root, prev_node):
            if root is None:
                return
            if prev_node:
                root.val = root.val + prev_node.val
            if root.left:
                dfs(root.left, root)
            if root.right:
                dfs(root.right, root)
            if root.left is None and root.right is None and root.val == targetSum:
                answer.append(True)
            
            return
        dfs(root, None)
        return any(answer)