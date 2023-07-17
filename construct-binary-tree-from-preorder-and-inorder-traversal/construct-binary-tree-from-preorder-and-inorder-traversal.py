# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {v:i for i,v in enumerate(inorder)}
        def recursive_search(low,high):
            if low>high:
                return None
            new_node = TreeNode(preorder.pop(0))
            mid_index = inorder_index[new_node.val]
            new_node.left = recursive_search(low, mid_index-1)
            new_node.right = recursive_search(mid_index+1,high)
            return new_node
        return recursive_search(0,len(inorder)-1)