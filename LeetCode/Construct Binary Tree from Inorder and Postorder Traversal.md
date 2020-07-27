### Given inorder and postorder traversal of a tree, construct the binary tree.

### Note:
- You may assume that duplicates do not exist in the tree.

```
For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
```

---

### Code:

### C++:

- Time complexity O(n2)
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
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        if(inorder.size()<0 && postorder.size()<0)
            return nullptr;
        
        return buildbt(postorder.size()-1,0,inorder.size()-1,inorder,postorder);
    }
    TreeNode* buildbt(int postStart,int inStart,int inEnd,vector<int>& inorder, vector<int>& postorder){
        if(inStart>inEnd) return nullptr;
        
        TreeNode* root = new TreeNode(postorder[postStart]);
        
        int inIndex = inStart;
        while(postorder[postStart] != inorder[inIndex]) inIndex++;
        
        root->left = buildbt(postStart-(inEnd-inIndex)-1,inStart,inIndex-1,inorder,postorder);
        root->right = buildbt(postStart-1,inIndex+1,inEnd,inorder,postorder);
        
        return root;
    }
};
```

### Other way:

- Time and Space complexity O(n)

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
    map<int,int> hasmap;
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
       if(inorder.size()<0 && postorder.size()<0)
            return nullptr;
        
        for(int i=0;i<inorder.size();i++)
            hasmap.insert({inorder[i],i});
        
        return buildbt(postorder.size()-1,0,inorder.size()-1,inorder,postorder);
    }
    TreeNode* buildbt(int postStart,int inStart,int inEnd,vector<int>& inorder, vector<int>& postorder){
        if(inStart>inEnd) return nullptr;
        
        TreeNode* root = new TreeNode(postorder[postStart]);
        
        int inIndex = hasmap[postorder[postStart]];
        //while(postorder[postStart] != inorder[inIndex]) inIndex++;
        
        root->left = buildbt(postStart-(inEnd-inIndex)-1,inStart,inIndex-1,inorder,postorder);
        root->right = buildbt(postStart-1,inIndex+1,inEnd,inorder,postorder);
        
        return root;
    }
};
```

### Python:

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder)<0 and len(postorder)<0:
            return None;
        
        def buildbt(postStart,inStart,inEnd,inorder,postorder):
            if inStart>inEnd: return None

            root = TreeNode(postorder[postStart])

            inIndex = inStart
            while postorder[postStart] != inorder[inIndex]: inIndex+=1

            root.left = buildbt(postStart-(inEnd-inIndex)-1,inStart,inIndex-1,inorder,postorder)
            root.right = buildbt(postStart-1,inIndex+1,inEnd,inorder,postorder)

            return root
        
        return buildbt(len(postorder)-1,0,len(inorder)-1,inorder,postorder)
    
    
```
