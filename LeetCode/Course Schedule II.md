### There are a total of n courses you have to take, labeled from 0 to n-1.

### Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

### Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

### There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

```
Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
```
```
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
```
### Note:

- The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
-You may assume that there are no duplicate edges in the input prerequisites.

### hint1:
- This problem is equivalent to finding the topological order in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.

### hint2:
-Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.

### hint3:
-Topological sort could also be done via BFS.

---

### Code:

### C++:

```
class Solution {
    bool cycle(int u, vector<vector<int>>& adj, vector<int>& s, vector<int>& visited){
        if (u >= adj.size())
            return false;
        
        if (visited[u])
            return visited[u] == 1;
        visited[u] = 1;
        for(int v : adj[u]){
            if(visited[v] == 1) return true;
            if(visited[v] == 0 && cycle(v,adj,s,visited)) return true;
        }
        visited[u] = 2;
        s.push_back(u);
        return false;
    }
public:
    Solution() {
        ios::sync_with_stdio(false); 
        cin.tie(NULL); 
        cout.tie(NULL);
    }
    
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
       vector<vector<int>> adj(numCourses);
        for(auto pre:prerequisites)
            adj[pre[1]].push_back(pre[0]);
        
        vector<int> s;
        vector<int> visited(numCourses, 0);
        for(int i=0;i<numCourses;++i)
            if(visited[i] == 0 && cycle(i,adj,s,visited)) return {};
        reverse(s.begin(),s.end());
        return s;
    }
};
```

### Python:

```
class Solution:
    def dfs(self, u: int):
        self.visited[u] = 1
        for v in self.adj[u]:
            if self.visited[v] == 1: return True
            if self.visited[v] == 0 and self.dfs(v): return True
            
        self.visited[u] = 2
        self.s.append(u)
        return False
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.adj = [[] for i in range(numCourses)]
        for c in prerequisites:
            self.adj[c[1]].append(c[0])
        
        self.s = []
        self.visited = [0]*numCourses
        for i in range(numCourses):
            if self.visited[i] == 0 and self.dfs(i): return []
        
        self.s.reverse()
        return self.s
```
