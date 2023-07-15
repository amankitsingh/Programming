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
            temp = []
            for i in curr_node:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            if temp:
                stack.append(temp)
            temp = []
            for i in curr_node:
                temp.append(i.val)
            answer.append(temp)
        return answer

# Answer 2
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
