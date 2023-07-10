# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def print_list(head):
            temp1 = head
            while temp1:
                print(f"{temp1.val}->",end="")
                temp1 = temp1.next
            print()
        def reverse_list(head, mid):
            temp1 = new_head = head
            count = 1
            while temp1 and count != mid:
                    rev = temp1.next
                    temp1.next = rev.next
                    rev.next = new_head
                    new_head = rev
                    count+=1
            head = new_head
            return [head,temp1.next]
            
        temp = head
        count = 0
        while temp:
            count+=1
            temp = temp.next
        
        if count == 1:
            return True
        
        mid = count//2
        head,mid_head = reverse_list(head, mid)
        temp_mid = mid_head
        
        mid_head = mid_head if count%2 == 0 else mid_head.next
        
        while head!=temp_mid:
            if head.val != mid_head.val:
                return False
            head = head.next
            mid_head = mid_head.next
        return True
        