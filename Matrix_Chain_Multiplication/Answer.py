### Answer 1 - Memoization approach
### Time complexity - O(N*N*N), Space complexity - O(N*N+N)
def mcm(arr,N):
    i=1
    j=N
    
    dp = [[-1]*(N+1) for k in range(N+1)]
    def recr(i,j):
        if i >= j:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        mini = float("inf")
        for k in range(i,j):
            res = recr(i,k)+recr(k+1,j) + arr[i-1]*arr[k]*arr[j]
            mini = min(mini, res)
        dp[i][j] = mini
        return dp[i][j]
    return recr(i,j)

### Answer 2 - tabulation approach
### Time complexity - O(N*N*N), Space complexity - O(N*N)
def mcm(p,n):
    n=n+1
    dp = [[-1]*(n) for i in range(n)]
    for i in range(n):
        dp[i][i] = 0
    for i in range(n-1,0,-1):
        for j in range(i+1,n):
            mini = float("inf")
            for k in range(i,j):
                res = dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j]
                mini = min(mini, res)
            dp[i][j]=mini
    
    return dp[1][n-1]

