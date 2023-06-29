# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        stack = collections.deque()
        stack.append((root,1))

        while stack:
            top_node,depth = stack.popleft()
            if top_node.left == None and top_node.right == None:
                return depth
            if top_node.left:
                stack.append((top_node.left,depth+1))
            if top_node.right:
                stack.append((top_node.right,depth+1))
        
