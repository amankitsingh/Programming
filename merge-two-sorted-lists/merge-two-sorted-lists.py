# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        head = ListNode(-10000)
        temp = head
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = ListNode(list1.val)
                temp = temp.next
                list1 = list1.next
            elif list1.val == list2.val:
                new_node = ListNode(list1.val,ListNode(list2.val))
                temp.next = new_node
                temp = temp.next.next
                list1 = list1.next
                list2 = list2.next
            else:
                temp.next = ListNode(list2.val)
                temp = temp.next
                list2 = list2.next
        if list1:
            while list1:
                temp.next = ListNode(list1.val)
                temp = temp.next
                list1 = list1.next
        if list2:
            while list2:
                temp.next = ListNode(list2.val)
                temp = temp.next
                list2 = list2.next
        return head.next