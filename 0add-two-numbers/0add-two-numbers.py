# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        temp = head
        
        while l1 and l2:
            sump = l1.val + l2.val + carry
            temp.next = ListNode(sump%10)
            carry = 1 if sump > 9 else 0
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            sump = l1.val + carry
            temp.next = ListNode(sump%10)
            carry = 1 if sump > 9 else 0
            temp = temp.next
            l1 = l1.next
        
        while l2:
            sump = l2.val + carry
            temp.next = ListNode(sump%10)
            carry = 1 if sump > 9 else 0
            temp = temp.next
            l2 = l2.next
        if carry:
            temp.next = ListNode(carry)
        return head.next