# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def search_node(root):
            if root == None:
                return
            search_node(root.left)
            search_node(root.right)
            result.append(root.val)
            return result
        
        result = []
        return search_node(root) if root else []
