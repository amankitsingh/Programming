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
