# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        decendent = {}
        stack = deque()
        decendent[root] = None
        stack.append(root)
        while stack:
            temp = stack.popleft()
            if temp.left:
                decendent[temp.left] = temp
                stack.append(temp.left)
            if temp.right:
                decendent[temp.right] = temp
                stack.append(temp.right)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = decendent[p]
        while q not in ancestors:
            q = decendent[q]
        return q