"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return
        temp = head

        while temp:
            temp.next = Node(temp.val,temp.next)
            temp = temp.next.next
        
        temp = head
        temp1 = head.next
        while temp:
            if temp.random:
                temp1.random = temp.random.next
            if temp1.next:
                temp = temp1.next
                temp1.next = temp.next
                temp1 = temp1.next
            else:
                temp = temp1.next
        
        return head.next
            
        
            