# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = deque()
        queue.append((root,0))
        
        while queue:
            node, level = queue.popleft()
            if node is None:
                continue
            if level<len(result):
                result[level].append(node.val)
            else:
                result.append([node.val])
            queue.append((node.left, level+1))
            queue.append((node.right, level+1))
        
        l = len(result)
        for k in range(1,l,2):
            result[k] = result[k][::-1]
        return result
            