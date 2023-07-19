# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverselist(head):
            if head and head.next:
                temp1 = head.next
                head.next = head.next.next
                temp1.next = self.temp
                self.temp = temp1
                reverselist(head)
            return self.temp
            
        self.temp = head
        return reverselist(head)