### Return the root node of a binary search tree that matches the given preorder traversal.

### (Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

### It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.
```
Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

```
### Constraints:

- 1 <= preorder.length <= 100
- 1 <= preorder[i] <= 10^8
- The values of preorder are distinct.

---

### Code:

### 1st way:
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
    TreeNode* buildbst(TreeNode* &root,int ele)
    {
        if(!root)
            return root= new TreeNode(ele);
        if(root->val>ele)
            buildbst(root->left,ele);
        else
            buildbst(root->right,ele);
        return root;
    }
  TreeNode* bstFromPreorder(vector<int>& preorder) {
    TreeNode *root = NULL;
      if(preorder.size()<=0)
          return NULL;
        for(auto x:preorder)
        {
            buildbst(root,x);
        }
        return root;}
};
```

### 2nd way:

```
TreeNode *getnode(int val)
    {
        TreeNode *newnode = new TreeNode;
        newnode->val = val;
        newnode->left = newnode->right = NULL;
        return newnode;
    }
    int buildbst(vector<int> &preorder,int n,int pos,TreeNode *curr,int left,int right)
    {
        if(pos==n || preorder[pos]<left || preorder[pos]>right)
            return pos;
        
        if(preorder[pos]<curr->val)
        {
            curr->left = getnode(preorder[pos]);
            pos+=1;
            pos = buildbst(preorder,n,pos,curr->left,left,curr->val-1);
        }
        if(pos==n || preorder[pos]<left || preorder[pos]>right)
            return pos;
        
        curr->right = getnode(preorder[pos]);
        pos+=1;
        pos=buildbst(preorder,n,pos,curr->right,curr->val+1,right);
        return pos;
        }
        TreeNode* bstFromPreorder(vector<int>& preorder) {
    
        int n= preorder.size();
        if(n==0)
            return NULL;
     TreeNode *root = new TreeNode(preorder[0]);
         if(n==1)
            return root;
        buildbst(preorder,n,1,root,INT_MIN,INT_MAX);
    return root;
    }
```
