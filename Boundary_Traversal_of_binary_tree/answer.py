### Answer 1 - Time complexity - O(H)+O(H)+O(H)~O(N), Space compelxity - O(N)
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def isleaf(self, root):
        return root.left is None and root.right is None

    def addleftboundary(self, root, result):
        temp = root.left
        while temp:
            if not self.isleaf(temp):
                result.append(temp.data)
            if temp.left:
                temp = temp.left
            else:
                temp = temp.right
    
    def addleafboundary(self, root, result):
        if self.isleaf(root):
            result.append(root.data)
        if root.left:
            self.addleafboundary(root.left, result)
        if root.right:
            self.addleafboundary(root.right, result)
        
    def addrightbundary(self,root, result):
        res = []
        temp = root.right
        while temp:
            if not self.isleaf(temp):
                res.append(temp.data)
            if temp.right:
                temp = temp.right
            else:
                temp = temp.left
        for k in res[::-1]:
            result.append(k)
    
    def printBoundaryView(self, root):
        result = []
        if root is None:
            result
        if not self.isleaf(root):
            result.append(root.data)
        
        self.addleftboundary(root, result)
        self.addleafboundary(root, result)
        self.addrightbundary(root, result)
        return result

