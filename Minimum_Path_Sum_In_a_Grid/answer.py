### Answer 1 - top - down approach
### Time complexity - O(N*M), space complexity - O(1) because of no extra space
def minSumPath(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i == 0 and j ==0:
                continue
            left,right = float("inf"),float("inf")
            if 0<=i-1<len(grid):
                left = grid[i][j]+grid[i-1][j]
            if 0<=j-1<len(grid[i]):
                right = grid[i][j]+grid[i][j-1]
            grid[i][j] = min(left,right)
    return grid[len(grid)-1][len(grid[0])-1]

### Answer 2 - bottom - up approach
### Time complexity - O(N*M), space complexity - O(M-1)+O(N-1)+O(M*N) stack space and dp

def minSumPath(grid):
    dp = [[-1 for j in range(m)] for i in range(n)]
    def findmin(i,j,dp):
        if dp[i][j]!=-1:
            return dp[i][j]
        if i == 0 and j == 0:
            return grid[i][j]
        if i < 0 or j < 0:
            return float("inf")
        up = grid[i][j] + findmin(i-1,j,dp)
        left = grid[i][j] + findmin(i,j-1,dp)
        dp[i][j] =  min(up,left)
        return dp[i][j]
    return findmin(len(grid)-1,len(grid[0])-1,dp)

### Answer 3 - top - down approach
### Time complexity - O(N*M), space complexity - N*O(M) ~ O(M) stack space and dp

def minSumPath(grid):
    n = len(grid)
    m = len(grid[0])
    prev = [0] * m
    for i in range(n):
        temp = [0]* m
        for j in range(m):
            if i == 0 and j == 0:
                temp[j] = grid[i][j]
                continue

            up = grid[i][j]
            if i > 0:
                up += prev[j]
            else:
                up = float("inf")
            
            left = grid[i][j]

            if j > 0:
                left += temp[j-1]
            else:
                left = float("inf")

            temp[j] = min(up,left)
        prev = temp
    return prev[m-1]
