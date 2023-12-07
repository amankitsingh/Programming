class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        queue = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i,j,0))

        maxi = 0
        while queue:
            i,j,minute = queue.popleft()
            maxi = max(maxi, minute)
            grid[i][j] = -1
            directions = [0,1,0,-1,0]
            for k in range(len(directions)-1):
                di,dj = i+directions[k], j+directions[k+1]
                if 0<= di < n and 0<= dj < m and grid[di][dj] == 1:
                    if (di,dj,minute) not in queue:
                        queue.append((di,dj,minute+1))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return maxi