# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        if temp is None or k == 0:
            return temp
        list_size = 1
        while temp.next:
            temp = temp.next
            list_size+=1
            
        temp.next = head
        k = list_size - (k % list_size)
        while k >0:
            temp = temp.next
            k-=1
        head,temp.next = temp.next,None
        return head
        
            
        
        