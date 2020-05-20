## Kth Smallest Element in a BST

### Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
```
Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
```
```
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
```

### Follow up:
### What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

---

Code:

```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int result;
    int index = -1;
    void findk(TreeNode* root, int &k){
        if(root == NULL)
            return;
        findk(root -> left, k);
        index ++;
        if(index == k-1)
            result = root -> val;
        else
            findk(root -> right, k);
    }
    int kthSmallest(TreeNode* root, int k) {
        findk(root, k);
        return result;
    }
};

/*
other way
int count = 0; 
    int ksmall = INT_MIN;
    TreeNode *curr = root;  
  
    while (curr != NULL) 
    {   if (curr->left == NULL) 
        { 
            count++; 
  
            if (count==k) 
                ksmall = curr->val; 
  
            curr = curr->right; 
        } 
        else
        { 
            TreeNode *pre = curr->left; 
            while (pre->right != NULL && pre->right != curr) 
                pre = pre->right; 
  
            if (pre->right==NULL) 
            { 
                pre->right = curr; 
                curr = curr->left; 
            } 
  
            else
            { 
                pre->right = NULL; 
  
                count++; 
                if (count==k) 
                    ksmall = curr->val; 
  
                curr = curr->right; 
            } 
        } 
    } 
    return ksmall;
 
*/
```
