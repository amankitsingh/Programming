# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## DFS
# Answer 1
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        answer = []
        def dfs(root, prev_node):
            if root is None:
                return
            if prev_node:
                root.val = root.val + prev_node.val
            if root.left:
                dfs(root.left, root)
            if root.right:
                dfs(root.right, root)
            if root.left is None and root.right is None and root.val == targetSum:
                answer.append(True)
            
            return
        dfs(root, None)
        return any(answer)

# Answer 2
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def f(root,s):
            if not root: return False
            if not root.left and not root.right: return root.val == s
            return f(root.left,s-root.val) or f(root.right,s-root.val)
        return f(root,targetSum) if root else False

# Answer 3
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, currentSum):
            #Base case
            if root == None:
                return False
            if root.left == None and root.right == None:
                return root.val + currentSum == targetSum
 

            #Logic
            currentSum += root.val
            left = dfs(root.left, currentSum)
            right = dfs(root.right, currentSum)

            return left or right
        
        return dfs(root, 0)
        
## BFS
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Iterative approach of dfs using stack

        if not root:
            return False

        #Use a stack to store path from root to current node
        stack = [(root,root.val)]

        while stack:
            node,val=stack.pop()

            # Check if the current node is a leaf node and its value matches the targetSum
            if not node.left and not node.right and val == targetSum:
                return True
            
            # Add the left and right children to the stack along with their updated path value
            if node.left:
                stack.append((node.left,val+node.left.val))
            if node.right:
                stack.append((node.right,val+node.right.val))
        
        return False
