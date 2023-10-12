class Solution:
    def search_neighbours(self, grid, i, j) -> int:
        directions = [0,1,0,-1,0]
        if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == "1":
            grid[i][j] = "0"
            for x in range(len(directions)-1):
                p,q = i+directions[x], j+directions[x+1]
                self.search_neighbours(grid,p,q)
            return 1
        return 0
    
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    result += self.search_neighbours(grid,i,j)
        
        return result