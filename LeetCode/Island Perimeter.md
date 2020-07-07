### You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

### Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

### The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

```
Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16
```

---

### Code:

### C++:
```
class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        ios_base::sync_with_stdio(nullptr);
        cin.tie(nullptr);
        cout.tie(nullptr);
        if(grid.size() == 0 || grid[0].size() ==0 ) return 0;
        int result = 0 ; 
        for(int i=0;i<grid.size();i++){
            for(int j=0;j<grid[i].size();j++){
                if(grid[i][j] == 1){
                    result+=4;
                
                if(i>0 && grid[i-1][j] == 1)
                    result-=2;
                if(j>0 &&  grid[i][j-1] == 1)
                    result-=2;
                }
            }
        }
        return result;
    }
};
```

### Python:

```
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        result = 0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                if grid[i][j] == 1:
                    result+=4
                    if i > 0 and grid[i-1][j] == 1:
                        result-=2
                    if j > 0 and grid[i][j-1] == 1:
                        result-=2
        return result
```
