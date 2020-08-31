### Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

### Basically, the deletion can be divided into two stages:

### Search for a node to remove.
### If the node is found, delete the node.
- Note: Time complexity should be O(height of tree).

```
Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
 ```
 
 ---
 
 ### Code:
 
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
     TreeNode* deleteNode(TreeNode* r, int x) {
       if(r == nullptr) return nullptr;
        if(r->val < x) {
            r->right = deleteNode(r->right, x);
        } else if(r->val > x) {
            //r->lc--;
            r->left = deleteNode(r->left, x);
        } else {
            if(r->right != nullptr && r->left != nullptr) {
                TreeNode* t = r->left;
                while(t->right != nullptr) t = t->right;
                r->val = t->val;
                r->left = deleteNode(r->left, t->val);
                return r;
            }
            if(r->left != nullptr) return r->left;
            return r->right;
        }
        return r;
    }
};
 ```
