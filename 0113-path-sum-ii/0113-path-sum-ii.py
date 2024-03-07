# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        def dfs(root, sump, lis):
            if root:
                if root.left is None and root.right is None and root.val == sump:
                    lis.append(root.val)
                    result.append(lis)
                dfs(root.left, sump-root.val, lis+[root.val])
                dfs(root.right, sump-root.val, lis+[root.val])
            
        dfs(root, targetSum, [])
        return result