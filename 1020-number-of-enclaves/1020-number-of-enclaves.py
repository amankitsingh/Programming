### Answer 1
### Time complexity - O(N*M*4)~O(N*M), Space complexity - O(1)
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def change_the_value(x,y):
            grid[x][y] = 0
            directions = [0,1,0,-1,0]
            for k in range(4):
                dx,dy = x+directions[k],y+directions[k+1]
                if 0<=dx<n and 0<=dy<m and grid[dx][dy] == 1:
                    change_the_value(dx,dy)

        for i in range(n):
            for j in range(m):
                if (i==0 or j==0 or i==n-1 or j==m-1)and grid[i][j] == 1:
                    change_the_value(i,j)


        count = 0
        for i in range(n):
            for j in range(m):
                if 0<=i<n and 0<=j<m and grid[i][j] == 1:
                    count+=1
        return count
        
### Answer 2
### just another way to code
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def change_the_value(x,y):
            if 0<=x<n and 0<=y<m and grid[x][y] == 1:
                grid[x][y] = 0
                directions = [0,1,0,-1,0]
                for k in range(4):
                    dx,dy = x+directions[k],y+directions[k+1]
                    if 0<=dx<n and 0<=dy<m and grid[dx][dy] == 1:
                        change_the_value(dx,dy)


                    
        for i in range(n):
            change_the_value(i,0)
            change_the_value(i,m-1)
            
        for i in range(m):
            change_the_value(0,i)
            change_the_value(n-1,i)
            
      
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count+=1
        return count
