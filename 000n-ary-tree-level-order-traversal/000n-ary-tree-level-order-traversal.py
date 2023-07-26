"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        result = []
        queue = deque()
        queue.append((root,0))
        while queue:
            temp,index = queue.popleft()
            if len(result) <= index:
                result.append([])
            result[index].append(temp.val)
            for child in temp.children:
                queue.append((child,index+1))
        return result
        