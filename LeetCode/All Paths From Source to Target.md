### Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

### The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

```
Example:
Input: [[1,2], [3], [3], []] 
Output: [[0,1,3],[0,2,3]] 
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
```

### Note:

- The number of nodes in the graph will be in the range [2, 15].
- You can print different paths in any order, but you should keep the order of nodes inside one path.

---

### Code:

### C++:

```
class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        vector<vector<int>> result;
        vector<int> temp;
        dfs(result,temp,0,graph);
        return result;
    }
    void dfs(vector<vector<int>>& result,vector<int>& temp,int index,vector<vector<int>>& graph){
        temp.push_back(index);
        
        if(!graph[index].size()){
            result.push_back(temp);
            return;
        }
        for(auto next:graph[index]){
            dfs(result,temp,next,graph);
            temp.pop_back();
        }
    }
};
```

### Python:

```
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        end = len(graph) - 1
        
        def dfs(index,path,result):
            if index == end:
                result.append(path)
                
            for curr in graph[index]:
                dfs(curr,path+[curr],result)
                
        result = []
        dfs(0,[0],result)
        return result
```
