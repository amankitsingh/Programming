# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        stack = deque()
        answer = []
        stack.append(root)
        while stack:
            temp = stack.popleft()
            if temp:
                answer.append(str(temp.val))
                stack.append(temp.left if temp.left else None)
                stack.append(temp.right if temp.right else None)
            else:
                answer.append("null")
        return ",".join(answer)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = [None if val == "null" else TreeNode(int(val))
             for val in data.split(',')]
        offset = 0
        for i in range(len(nodes)):
            if nodes[i]:
                nodes[i].left = nodes[i+1+offset] if i+1+offset < len(nodes) else None
                nodes[i].right = nodes[i+2+offset] if i+2+offset < len(nodes) else None
                offset+=1

            else:
                offset-=1
        return nodes[0]

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))