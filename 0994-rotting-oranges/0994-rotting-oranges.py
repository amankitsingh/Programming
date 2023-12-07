class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        queue = deque()
        total = days = count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] != 0:
                    total+=1

        maxi = 0
        while queue:
            lenp = len(queue)
            count+=lenp
            while lenp > 0:
                lenp-=1
                i,j = queue.popleft()
                directions = [0,1,0,-1,0]
                for k in range(len(directions)-1):
                    di,dj = i+directions[k], j+directions[k+1]
                    if 0<= di < n and 0<= dj < m and grid[di][dj] == 1:
                        grid[di][dj] = 2
                        queue.append((di,dj))
            if queue:
                days+=1

        return days if total == count else -1