# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Answer 1
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root and root.val == val:
            return root
        else:
            if root:
                temp1 = self.searchBST(root.left,val)
                temp2 = self.searchBST(root.right,val)
                return temp1 if temp1 and temp1.val == val else temp2
            else:
                return None
        
        return self.searchBST(root,val) 

# Answer 2
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val < val:
            return self.searchBST(root.right,val)
        elif root.val > val:
            return self.searchBST(root.left,val)
        return root

# Answer 3
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None or root.val==val:
            return root
        return self.searchBST(root.left,val) if root.val>val else self.searchBST(root.right,val)
        
