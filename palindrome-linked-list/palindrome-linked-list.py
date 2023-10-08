## Better approach
#class ListNode:
#	def __init__(self, val=0, next=None):
#		self.val = val
#		self.next = next

class Solution:
	def isPalindrome(self, head):
    rev = None
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
    while rev and rev.val == slow.val:
        slow = slow.next
        rev = rev.next
    return not rev


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
            
        # Time complexity - O(logn)
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
        # count the number of element in the list O(n)
        while temp:
            count+=1
            temp = temp.next
        
        # if one return true
        if count == 1:
            return True
        
        # Take the middle element and reverse the list from beginning to middle
        mid = count//2
        head,mid_head = reverse_list(head, mid)
        temp_mid = mid_head
        
        # if even then check from beginning and middle, else beginning and next element to middle
        mid_head = mid_head if count%2 == 0 else mid_head.next
        
        # check from beginning and new middle
        # Time complexity O(logn)
        while head!=temp_mid:
            if head.val != mid_head.val:
                return False #if any element is an mismatach then false
            head = head.next
            mid_head = mid_head.next
        return True # Time complexity = O(n) + O(logn) + O(logn) = O(n) because the linear term dominates the logarithmic terms as the input size grows.
        
