# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def areIdentical(self, root1, root2):
        if root1 is None or root2 is None:
            return root1 == None and root2 == None
        return (root1.val == root2.val and self.areIdentical(root1.left, root2.left) and self.areIdentical(root1.right,root2.right))
    

    def isSubtree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root2 is None:
            return True
        if root1 is None:
            return False
        
        if self.areIdentical(root1, root2):
            return True
        
        return self.isSubtree(root1.left, root2) or self.isSubtree(root1.right, root2)