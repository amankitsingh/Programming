# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None: return False
        
        while head.next:
            if head.val is False:
                return True
            else:
                head.val = False
                head = head.next
        return False