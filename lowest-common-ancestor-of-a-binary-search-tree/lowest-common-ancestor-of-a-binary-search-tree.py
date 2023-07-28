# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        decedent = {}
        stack = deque()
        decedent[root] = None
        stack.append(root)
        while stack:
            temp = stack.popleft()
            if temp.left:
                decedent[temp.left] = temp
                stack.append(temp.left)
            if temp.right:
                decedent[temp.right] = temp
                stack.append(temp.right)
        ancestor = set()
        while p:
            ancestor.add(p)
            p = decedent[p]
        while q not in ancestor:
            q = decedent[q]
        return q
            

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root:
            if min(p.val,q.val) <= root.val <= max(p.val,q.val):
                return root
            elif max(p.val,q.val) < root.val:
                return self.lowestCommonAncestor(root.left, p,q)
            elif min(p.val,q.val) > root.val:
                return self.lowestCommonAncestor(root.right, p,q)
