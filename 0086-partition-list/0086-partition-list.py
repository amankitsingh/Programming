# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        pre,post = ListNode(0),ListNode(0)
        pre_point,post_point=pre,post
        
        while head:
            if head.val < x:
                pre_point.next,pre_point = head,head
            else:
                post_point.next,post_point = head,head
            head = head.next
            
        post_point.next = None
        pre_point.next = post.next
        return pre.next