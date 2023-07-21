# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Answer 1 - Time complexity O(m+n) - space complexity: O(m+n)
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

#Answer2 - Time complexity: O(m+n) - space complexity: O(1)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        temp = head
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                temp = temp.next
                list1 = list1.next
            else:
                temp.next = list2
                temp = temp.next
                list2 = list2.next
    
        
        while list1:
            temp.next = list1
            temp = temp.next
            list1 = list1.next
        while list2:
            temp.next = list2
            temp = temp.next
            list2 = list2.next
        return head.next

# Answer 3 - Recursive Time complexity O(m+n) - Space complexity O(1)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:        
        if not list1: return list2
        if not list2: return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
