### Answer 1 - top - down approach, iterate from bottom up
### Time complexity - O(N*M), space complexity - O(N) + O(N*M)
def getMaxPathSum(matrix):
    m = len(matrix)
    n = len(matrix[0])
    dp = [[-1 for i in range(n)] for j in range(m)]
    def findmax(i,j):
        if j < 0 or j >= n:
            return float("-inf")

        if i == 0:
            return matrix[0][j]

        if dp[i][j]!=-1:
            return dp[i][j]
        
        directions = [(-1,0),(-1,-1),(-1,1)]
        maxi = float("-inf")
        for p,q in directions:
            new_x = i + p
            new_y = j + q
            maxi = max(maxi, matrix[i][j] + findmax(new_x,new_y))
        dp[i][j] = maxi
        return dp[i][j]

    maxi = float("-inf")
    for j in range(n):
        ans = findmax(m-1,j)
        maxi = max(maxi,ans)
    return maxi

### Answer 2 - top - down approach
### Time complexity - O(N*M), space complexity - O(N*M)
def getMaxPathSum(matrix):
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0 for i in range(n)] for j in range(m)]
    for i in range(n):
        dp[0][i] = matrix[0][i]
    
    for i in range(1,m):
        for j in range(n):
            up = matrix[i][j] + dp[i-1][j]
            leftdig = matrix[i][j]
            if j - 1 >= 0:
                leftdig+=dp[i-1][j-1]
            else:
                leftdig = float("-inf")
            
            rightdig = matrix[i][j]
            if j + 1 < n:
                rightdig += dp[i-1][j+1]
            else:
                rightdig = float("-inf")
            
            dp[i][j] = max(up, leftdig, rightdig)
    return max(dp[m-1])

### Answer 3 - top - down approach
### Time complexity - O(N*M), space complexity - O(N)
def getMaxPathSum(matrix):
    m = len(matrix)
    n = len(matrix[0])
    prev = [0]*n
    cur = [0]*n
    for i in range(n):
        prev[i] = matrix[0][i]
    
    for i in range(1,m):
        for j in range(n):
            up = matrix[i][j] + prev[j]
            leftdig = matrix[i][j]
            if j - 1 >= 0:
                leftdig+=prev[j-1]
            else:
                leftdig = float("-inf")
            
            rightdig = matrix[i][j]
            if j + 1 < n:
                rightdig += prev[j+1]
            else:
                rightdig = float("-inf")
            
            cur[j] = max(up, leftdig, rightdig)
        prev = cur[:]
    return max(prev)
