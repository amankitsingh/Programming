# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Answer 1
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        stack = deque()
        answer = []
        stack.append([root])
        while stack:
            curr_node = stack.popleft()
            temp,result = [],[]
            for i in curr_node:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
                result.append(i.val)
            if temp:
                stack.append(temp)
            if result:
                answer.append(result)
        return answer

# Answer 2
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[float]:
        numbers = []
        queue = [(root, 0)]
        while queue:
            node, depth = queue.pop(0)
            if node is None:
                continue
            if depth < len(numbers):
                numbers[depth].append(node.val)
            else:
                numbers.append([node.val])
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))
        return numbers
