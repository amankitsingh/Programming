# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def findorder(root):
            if not root:
                return
            findorder(root.left)
            result.append(root.val)
            findorder(root.right)
        
        findorder(root)
        return result