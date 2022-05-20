# Solution 1: Recursive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfh(root, level=0):
            if root is None:
                return level
            return max(dfh(root.left,level+1),dfh(root.right,level+1))
        return dfh(root)
    
# Solution 2: Iterative

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        que = deque([root])
        level = 0
        while que:
            level+=1
            for _ in range(len(que)):
                temp = que.popleft()
                if temp.left:
                    que.append(temp.left)
                if temp.right:
                    que.append(temp.right)
                    
         return level
