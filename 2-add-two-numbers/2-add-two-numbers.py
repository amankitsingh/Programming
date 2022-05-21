# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        temp = ListNode()
        root = temp
        while l1 and l2:
            total = l1.val + l2.val + carry
            carry = 0
            if total > 9:
                carry = 1
            
            temp.next = ListNode(total % 10)
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        
        if l1:
            if carry:
                while l1:
                    total = l1.val + carry
                    carry = 0
                    if total > 9:
                        carry = 1
                        
                    temp.next = ListNode(total % 10)
                    temp = temp.next
                    l1 = l1.next
            else:
                temp.next = l1
                    
                    
        if l2:
            if carry:
                while l2:
                    total = l2.val + carry
                    carry = 0
                    if total > 9:
                        carry = 1
                    
                    temp.next = ListNode(total % 10)
                    temp = temp.next
                    l2 = l2.next
            else:
                temp.next = l2
                
        if carry:
            temp.next = ListNode(1)
            
        return root.next