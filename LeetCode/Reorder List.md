### Given a singly linked list L: L0→L1→…→Ln-1→Ln,
### reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

### You may not modify the values in the list's nodes, only nodes itself may be changed.
```
Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
```
```
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
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
    void reorderList(ListNode* head) {
         if(head != NULL && head->next != NULL && (head->next)->next != NULL){
            vector <ListNode*> v;
            ListNode *cur = head;
            while(cur){v.push_back(cur);cur=cur->next;}   //create vector with pointers
            int begin=0,end=v.size() - 1; 
            int half=(end+1)/2;
            for(begin;begin<half;end--){                           
                v[begin]->next = v[end];                                  // reorder list
                v[end]->next = v[++begin]; 
            }
            v[begin]->next = NULL;
        }
    }
};
```

### Other way:

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
    void reorderList(ListNode* head) {
        if(!head)
            return ;
        map<int,ListNode*> m;
        int count=1;
        while(head!=NULL)
        {
            m[count++]=head;
            head=head->next;
        }
        --count;
        int start=1,end=count;
        while(start<end)
        {
            m[start]->next=m[end];
            ++start;
            if(start<end)
                m[end]->next=m[start];
            else m[end]->next=NULL;
            --end;
        }
        if(count&1)
            m[start]->next=NULL;
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
    def reorderList(self, head):
        #step 1: find middle
        if not head: return []
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        #step 2: reverse second half
        prev, curr = None, slow.next
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt    
        slow.next = None
        
        #step 3: merge lists
        head1, head2 = head, prev
        while head2:
            nextt = head1.next
            head1.next = head2
            head1 = head2
            head2 = nextt
        
```
