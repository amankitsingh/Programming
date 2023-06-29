# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def search_node(root):
            if root == None:
                return
            result.append(root.val)
            search_node(root.left)
            search_node(root.right)
            return result
        result = []
        return search_node(root) if root else []
