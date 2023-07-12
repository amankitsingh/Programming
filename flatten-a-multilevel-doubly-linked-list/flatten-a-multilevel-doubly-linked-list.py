"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def children(self, temp):
        while temp and temp.next:
            temp = temp.next
        return temp
    def print_list(self, temp):
        while temp:
            print(temp.val,temp.prev,temp,temp.next)
            temp = temp.next
            
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head
        while temp:
            if temp.child:
                temp.child.prev = temp
                child_end = self.children(temp.child)
                if temp.next:
                    temp_next = temp.next
                    temp.next,temp_next.prev = temp.child, child_end
                    child_end.next=temp_next
                else:
                    temp.next = temp.child
                temp.child = None
            temp = temp.next
       # self.print_list(head)
        return head