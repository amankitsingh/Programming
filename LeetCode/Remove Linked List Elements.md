### Remove all elements from a linked list of integers that have value val.

```
Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
```

---

### Code:

### C++:

```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        if(!head) return nullptr;
        while(head && head->val == val)
            head = head->next;

        ListNode* temp = head;
        while(temp && temp->next){
            if(temp->next->val == val)
                temp->next = temp->next->next;
            else
                temp = temp->next;
        }
        return head;
    }
};
```

### Python:

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head: return None
        while head and head.val == val:
            head = head.next
        self.temp = head
        while self.temp and self.temp.next:
            if self.temp.next.val == val:
                self.temp.next = self.temp.next.next
            else:
                self.temp = self.temp.next
        return head
```
