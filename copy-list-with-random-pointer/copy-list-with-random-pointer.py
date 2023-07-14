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
        d = {None : None}
        temp = head

        while(temp):
            new_node = Node(temp.val)
            d[temp] = new_node
            temp = temp.next
        
        temp = head
        new_head = d[head]

        while(temp):
            d[temp].next = d[temp.next]
            d[temp].random = d[temp.random]
            temp = temp.next 

        return new_head
        
        
            