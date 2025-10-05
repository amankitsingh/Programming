# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import queue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = queue.PriorityQueue()
        counter = 0
        for node in lists:
            if node:
                pq.put((node.val, counter, node))
                counter+=1
        
        dummyNode = ListNode(-1)
        temp = dummyNode

        while not pq.empty():
            _, _, current_node = pq.get()
            temp.next = current_node
            temp = temp.next
            if current_node.next:
                pq.put((current_node.next.val, counter, current_node.next))
                counter+=1
        
        return dummyNode.next
