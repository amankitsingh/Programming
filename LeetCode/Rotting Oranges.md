### In a given grid, each cell can have one of three values:

- the value 0 representing an empty cell;
- the value 1 representing a fresh orange;
- the value 2 representing a rotten orange.
- Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

### Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

```
Example 1:
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
```
```
Example 2:
Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
```
```
Example 3:
Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
```

### Note:

- 1 <= grid.length <= 10
- 1 <= grid[0].length <= 10
- grid[i][j] is only 0, 1, or 2.

### Code:

### C++:

```
auto i1 = []()
{
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        cout.tie(NULL);
        return 0;
}();
class Solution {
    typedef pair<int,pair<int,int>> p;
public:
    int orangesRotting(vector<vector<int>>& grid) {
        queue<p> q;
        
        int n = grid.size();
        int m = grid[0].size();
        int count = 0;
        
        for(int i=0;i<n;++i){
            for(int j=0;j<m;++j){
                if(grid[i][j] == 2)
                    q.push({0,{i,j}});
            }
        }
        
        while(!q.empty()){
            p temp = q.front();
            count = temp.first;
            
            int x = temp.second.first;
            int y = temp.second.second;
            
            if(x+1<n){
                if(grid[x+1][y] == 1){
                    grid[x+1][y] = 2;
                    q.push({count+1,{x+1,y}});
                }
            }
            if(x-1>=0){
                if(grid[x-1][y] == 1){
                    grid[x-1][y] = 2;
                    q.push({count+1,{x-1,y}});
                }
            }
            
            if(y-1>=0){
                if(grid[x][y-1]==1){
                    grid[x][y-1] = 2;
                    q.push({count+1,{x,y-1}});
                }
            }
            
            if(y+1<m){
                if(grid[x][y+1] == 1){
                    grid[x][y+1] = 2;
                    q.push({count+1,{x,y+1}});
                }
            }
            q.pop();
        }
        
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                if(grid[i][j] == 1)
                    return -1;
        return count;
    }
};
```

### Python:

```
class Solution:
    def orangesRotting(self, grid):
        m, n, queue, fresh = len(grid), len(grid[0]), deque(), 0
        for i,j in product(range(m), range(n)):
            if grid[i][j] == 2: queue.append((i,j))
            if grid[i][j] == 1: fresh += 1
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        levels = 0
        
        while queue:
            levels += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in dirs:
                    if 0<=x+dx<m and 0<=y+dy<n and grid[x+dx][y+dy] == 1:
                        fresh -= 1
                        grid[x+dx][y+dy] = 2
                        queue.append((x+dx, y+dy))
                        
        return -1 if fresh != 0 else max(levels-1, 0)
```
