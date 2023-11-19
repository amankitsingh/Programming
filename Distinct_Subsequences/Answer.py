### Answer 1:
### Time complexity - O(N*M), Space complexity - O(N*M)+O(N+M)
def distinctSubsequences(stri: str, sub: str) -> int:
    n = len(stri)
    m = len(sub)
    dp = [[-1]*(m+1) for _ in range(n+1)]
    def helper(index1, index2):

        if index2 < 0:
            return 1
        if index1 < 0:
            return 0
        
        if dp[index1][index2]!=-1:
            return dp[index1][index2]
        
        if stri[index1] == sub[index2]:
            dp[index1][index2] = (helper(index1-1, index2-1) + helper(index1-1,index2))
        else:
            dp[index1][index2] = helper(index1-1, index2)
        
        return dp[index1][index2]
    
    return helper(n-1,m-1)%int(1e9 + 7)

### Answer 2:
### Time complexity - O(N*M), Space complexity - O(N*M)
def distinctSubsequences(stri: str, sub: str) -> int:
    n = len(stri)
    m = len(sub)
    dp = [[0]*(m+1) for _ in range(n+1)]

    for _ in range(n+1):
        dp[_][0] = 1
    
    for index1 in range(1,n+1):
        for index2 in range(1, m+1):
            if stri[index1-1] == sub[index2-1]:
                dp[index1][index2] = (dp[index1-1][index2-1] + dp[index1-1][index2])
            else:
                dp[index1][index2] = dp[index1-1][index2]
                
    return dp[n][m]%int(1e9 + 7)


### Answer 3:
### Time complexity - O(N*M), Space complexity - O(M)
def distinctSubsequences(stri: str, sub: str) -> int:
    n = len(stri)
    m = len(sub)
    prev = [0]*(m+1)

    prev[0] = 1
    
    for index1 in range(1,n+1):
        for index2 in range(m,0,-1):
            if stri[index1-1] == sub[index2-1]:
                prev[index2] = prev[index2-1] + prev[index2]
            else:
                prev[index2] = prev[index2]
                
    return prev[m]%int(1e9 + 7)
