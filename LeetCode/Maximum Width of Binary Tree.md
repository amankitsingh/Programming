### Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

### The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

```
Example 1:

Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
```
```
Example 2:

Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
```
```
Example 3:

Input: 

          1
         / \
        3   2 
       /        
      5      

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
```
```
Example 4:

Input: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).
```
- Note: Answer will in the range of 32-bit signed integer.

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
public:
    int widthOfBinaryTree(TreeNode* root) {
        ios::sync_with_stdio(false); 
        cin.tie(0); 
        cout.tie(0);
        if(!root) return 0;
        int result = 1;
        queue<pair<TreeNode*,int>> Q;
        Q.push({root,0});
        while(!Q.empty()){
            int count = Q.size();
            int start = Q.front().second;
            int end = Q.back().second;
            result = max(result,end-start+1);
            while(count){
                pair<TreeNode *,int> p = Q.front();
                int idx = p.second - start;
                Q.pop();
                if(p.first->left) Q.push({p.first->left,2*idx+1});
                if(p.first->right) Q.push({p.first->right,2*idx+2});
                count-=1;
            }
        }
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
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if root == None: return 0
        result = 1
        Q = [[root, 0]]
        while len(Q) > 0:
            count = len(Q)
            start = Q[0][1]
            end = Q[-1][1]
            result = max(result, end-start+1)
            for i in range(count):
                p = Q[0]
                idx = p[1]
                Q.pop(0)
                if (p[0].left != None): Q.append([p[0].left, 2*idx+1])
                if p[0].right != None: Q.append([p[0].right, 2*idx+2])
            
        return result
```
