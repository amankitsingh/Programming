### Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

```
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

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
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if(root == nullptr) return result;
        stack<TreeNode*> s1;
        stack<TreeNode*> s2;
        
        s1.push(root);
        vector<int> list;
        while(!s1.empty() || !s2.empty()){
            while(!s1.empty()){
                TreeNode* temp = s1.top();
                s1.pop();
                list.push_back(temp->val);
                if(temp->left)
                    s2.push(temp->left);
                if(temp->right)
                    s2.push(temp->right);
            }
            if(!list.empty())
                result.push_back(list);
            list.clear();
            while(!s2.empty()){
                TreeNode* temp = s2.top();
                s2.pop();
                list.push_back(temp->val);
                if(temp->right)
                    s1.push(temp->right);
                if(temp->left)
                    s1.push(temp->left);
            }
             if(!list.empty())
                result.push_back(list);
            list.clear();
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        result = []
        if not root: return result
        s1,s2 = [],[]
        
        s1.append(root)
        lis = []
        while len(s1)>0 or len(s2)>0:
            while len(s1)>0:
                self.temp = s1.pop()
                lis.append(self.temp.val)
                if self.temp.left:
                    s2.append(self.temp.left)
                if self.temp.right:
                    s2.append(self.temp.right)

            if len(lis)>0:
                result.append(lis)
            lis = []
            while len(s2)>0:
                self.temp = s2.pop()
                lis.append(self.temp.val)
                if self.temp.right:
                    s1.append(self.temp.right)
                if self.temp.left:
                    s1.append(self.temp.left)
                    
            if len(lis)>0:
                result.append(lis)
            lis = []
        return result
```

### other way:
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        q, res = [], []
        if root != None:
            q.append(root)
        while len(q) > 0:
            curLevel = []
            for i in range(len(q)):
                node = q.pop(0)
                curLevel.append(node.val)
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            if len(res) % 2 != 0:
                for j in range(len(curLevel)//2):
                    curLevel[j], curLevel[len(curLevel)-1-j] = curLevel[len(curLevel)-1-j], curLevel[j]
            res.append(curLevel)
        return res
```
