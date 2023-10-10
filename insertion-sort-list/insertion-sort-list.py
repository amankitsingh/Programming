# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sort = ListNode() 

        cur = head
        while cur:
            sortCur = sort
            while sortCur.next and cur.val >= sortCur.next.val:
                sortCur = sortCur.next
                
            tmp, sortCur.next = sortCur.next, cur
            cur = cur.next
            sortCur.next.next = tmp
            
        return sort.next