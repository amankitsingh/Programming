# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return
        if head.val == val:
            while head:
                if head.val == val:
                    head = head.next
                else:
                    break
        prev = head
        temp = head
        while temp and temp.next:
            if temp.val == val:
                prev.next = temp.next
            else:
                prev = temp
            temp = temp.next
        
        if temp and temp.next is None:
            if temp.val == val:
                prev.next = None
        
        return head