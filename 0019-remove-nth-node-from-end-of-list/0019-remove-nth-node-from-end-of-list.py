# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer1,pointer2 = None, head
        
        while pointer2:
            n-=1
            pointer2 = pointer2.next
            if n == 0:
                pointer1 = head
                break
        if pointer2 is None and pointer1:
            return pointer1.next
        while pointer2.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
            
        pointer1.next = pointer1.next.next
        return head