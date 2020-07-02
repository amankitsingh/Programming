### Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

```
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
```

---

### Code:

### C++

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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> result;
        if(!root) return result;
        queue<TreeNode*> Q;
        Q.push(root);
        while(!Q.empty()){
            int n = Q.size();
            vector<int> nodes(n);
            for(int i=0;i<n;++i){
                TreeNode* node = Q.front();
                Q.pop();
                nodes[i] =  node -> val;
                if(node->left) Q.push(node->left);
                if(node->right) Q.push(node->right);
            }
            result.push_back(nodes);
        }
        reverse(result.begin(),result.end());
        return result;
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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root == None: return result
        Q = []
        Q.append(root)
        while len(Q)>0:
            nodes = []
            for i in range(len(Q)):
                node = Q.pop(0)
                nodes.append(node.val)
                if node.left != None: Q.append(node.left)
                if node.right != None: Q.append(node.right)
            result.insert(0,nodes)
        return result
```
