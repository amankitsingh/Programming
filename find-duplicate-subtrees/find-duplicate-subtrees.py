from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def traverse(root):
            if not root:
                return 0
            triplet = (traverse(root.left), root.val, traverse(root.right))
            if triplet not in triplet_to_id:
                triplet_to_id[triplet] = len(triplet_to_id) + 1
            id = triplet_to_id[triplet]
            counter[id]+=1
            if counter[id] == 2:
                result.append(root)
            return id                   
        triplet_to_id = {}
        counter = defaultdict(int)
        result = []
        traverse(root)
        return result