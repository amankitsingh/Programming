# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index_inorder= {v:i for i,v in enumerate(inorder)}
        def recursive_search(low,high):
            if low > high:
                return None
            new_node = TreeNode(postorder.pop())
            mid = index_inorder[new_node.val]
            new_node.right = recursive_search(mid+1, high)
            new_node.left = recursive_search(low,mid-1)
            return new_node
        return recursive_search(0, len(inorder)-1)