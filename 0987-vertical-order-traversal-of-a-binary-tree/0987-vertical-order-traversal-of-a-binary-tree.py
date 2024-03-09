# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        data_store = defaultdict(list)
        queue = deque()
        queue.append((root,0,0))
        
        while queue:
            node, vertical, level = queue.popleft()
            if node is None:
                continue
            data_store[(vertical, level)].append(node.val)
            data_store[(vertical, level)].sort()
            queue.append((node.left, vertical-1, level+1))
            queue.append((node.right, vertical+1, level+1))
        result = defaultdict(list)
        keys = sorted(list(data_store.keys()), key = lambda x: (x[0],x[1]))
        
        for data in keys:
            vert, depth = data
            result[vert].extend(data_store[data])
        return result.values()
    