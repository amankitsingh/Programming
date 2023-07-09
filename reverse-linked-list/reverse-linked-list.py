# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = head
        while head and head.next:
            temp = head.next
            head.next = temp.next
            temp.next = new_head
            new_head = temp
        return new_head