# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.traverse(root,0,result)
        return result
    
    def traverse(self,root,level,result):
        if not root:
            return
        
        if len(result) == level:
            result.append(root.val)
        
        self.traverse(root.right,level+1,result)
        self.traverse(root.left, level+1, result)
        return result
        
        