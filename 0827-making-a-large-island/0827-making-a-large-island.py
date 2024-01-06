### Answer 1 - Using DisJoint Set 
### Time complexity - O(N*N + N*N)~O(N), Space complexity - O(2*N*N)~O(N*N)
### Its a good method, but slightly slower than normal DFS search
class DisjointSet:
    def __init__(self, size):
        self.size = [1]*size
        self.parents = list(range(size))
    
    def findparent(self, node):
        if node != self.parents[node]:
            self.parents[node] = self.findparent(self.parents[node])
        return self.parents[node]
    
    def union(self, u, v):
        ulp_u, ulp_v = self.parents[u], self.parents[v]
        if ulp_u == ulp_v:
            return 
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parents[ulp_u] = ulp_v
            self.size[ulp_v]+=self.size[ulp_u]
        else:
            self.parents[ulp_v]= ulp_u
            self.size[ulp_u]+=self.size[ulp_v]
            
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # Taking the size as n*n to get the exact coordinate number of the cell
        total_size = n*n
        dsu = DisjointSet(total_size)
    
        def isValidRange(x,y):
            if 0<= x < n and 0<= y < n:
                return True
            return False
            
        def attach_other_cells(i,j):
            directions = [0,-1,0,1,0]
            for k in range(4):
                dx,dy=i+directions[k],j+directions[k+1]
                if isValidRange(dx,dy) and grid[dx][dy] == 1:
                    # this will give the exact coordiante of the column in the cell
                    # row*n+col
                    cell_number_from = i*n+j
                    cell_number_to = dx*n+dy
                    if dsu.findparent(cell_number_from) != dsu.findparent(cell_number_to):
                        dsu.union(cell_number_from, cell_number_to)
        
        unseen_directions = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    attach_other_cells(i,j)
                else:
                    unseen_directions.append([i,j])
        
        result = max(dsu.size)
        def find_largest_group(i,j):
            nonlocal result
            directions = [0,-1,0,1,0]
            temp = 0
            cell_number_from = i*n+j
            components = set()
            for k in range(4):
                dx,dy=i+directions[k],j+directions[k+1]
                if isValidRange(dx,dy) and grid[dx][dy] == 1:
                    cell_number_to = dx*n+dy
                    components.add(dsu.findparent(cell_number_to))
            
            for i in components:
                temp+=dsu.size[i]
            result = max(result,temp+1)
            
        for i,j in unseen_directions:
            find_largest_group(i,j)

        return result

### Answer 2 - Using DFS Search
### Time complexity - O(N*N + N*N)~O(N), Space complexity - O(S)
### Its a good method, but faster than disjoint set
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1, 0),(0,-1)]


        def dfs(r, c, i):
            count = 1
            grid[r][c] = i

            for dr, dc in directions:
                nr = dr+r
                nc = dc+c
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                    continue
                if grid[nr][nc] == 1:
                    count += dfs(nr, nc, i)

            return count


        max_size = 0
        sizes = {}
        i = 2
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    sizes[i] = dfs(r, c, i)
                    max_size = max(max_size, sizes[i])
                    i+=1
        
        if not sizes:
            return 1

        # now expand 
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 0:
                    continue

                cur_size = 1
                touches = set()
                for dr, dc in directions:
                    nr = dr+r
                    nc = dc+c
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc]==0:
                        continue
                    touches.add(grid[nr][nc])

                for island in touches:
                    cur_size+=sizes[island]
                max_size = max(max_size, cur_size)

        return max_size
        
