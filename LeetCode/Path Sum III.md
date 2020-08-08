### You are given a binary tree in which each node contains an integer value.

### Find the number of paths that sum to a given value.

### The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

### The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

```
Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
```

---

### Code:

### C++:

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
    int path_sum(TreeNode* root,int sum){
        if(!root) return 0;
        int res = 0;
        if(root->val == sum) res++;
        res += path_sum(root->left,sum-root->val);
        res += path_sum(root->right,sum-root->val);
        return res;
    }
public:
    int pathSum(TreeNode* root, int sum) {
        if(!root) return 0;
        return pathSum(root->left,sum) + path_sum(root,sum) + pathSum(root->right,sum);
    }
};
```

### Other way:

```
class Solution {
public:
    int DFS(TreeNode *root,int sum){
        if(root==nullptr)
            return 0;
        int ans = root->val==sum?1:0;
        return ans + DFS(root->left,sum-root->val) + DFS(root->right,sum-root->val);
    }
    int pathSum(TreeNode* root, int sum) {
        if(root==nullptr)
            return 0;
        return DFS(root,sum) + pathSum(root->left,sum) + pathSum(root->right,sum);
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
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        def path_sum(root,sum):
            if root == None: return 0
            res = 0
            if root.val == sum: res+=1
            res += path_sum(root.left, sum-root.val)
            res += path_sum(root.right, sum-root.val)
            
            return res
        
        if root == None: return 0
        return self.pathSum(root.left,sum) + path_sum(root,sum) + self.pathSum(root.right, sum)
```
