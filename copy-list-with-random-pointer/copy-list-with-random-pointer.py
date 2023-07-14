"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# Answer 1 - Time complexity O(n), Space complexity O(n)
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
            
#Answer 2 - Time complexity O(n), Space complexity O(n+m) 
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
        
        
            
