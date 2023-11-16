### Core logic
"""
first we remove the element from s1 - which take n-k
second we add the element from s2 - which take m-k
result = n-k+m-k or (n+m)-2*k
"""
### Answer 1
### Time complexity - O(N*M), Space complexity - O(N+M)
def canYouMake(s1: str, s2: str) -> int:
    n = len(s1)
    m = len(s2)

    dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]

    def lcs(index1, index2):
        if index1 == n or index2 == m:
            return 0
        
        if dp[index1][index2]!=-1:
            return dp[index1][index2]
        if s1[index1] == s2[index2]:
            dp[index1][index2] = 1 + lcs(index1+1, index2+1)
        else:
            dp[index1][index2] = max(lcs(index1+1,index2), lcs(index1, index2+1))
        return dp[index1][index2]

    return (n+m)-(2*lcs(0,0))

### Answer 2
### Time complexity - O(N*M), Space complexity - O(N+M)
def canYouMake(s1: str, s2: str) -> int:
    n = len(s1)
    m = len(s2)

    dp = [[0]*(m+1) for _ in range(n+1)]

    for index1 in range(1,n+1):
        for index2 in range(1, m+1):
            if s1[index1-1] == s2[index2-1]:
                dp[index1][index2] = 1 + dp[index1-1][index2-1]
            else:
                dp[index1][index2] = max(dp[index1-1][index2], dp[index1][index2-1])
    return n+m-(2*dp[n][m])

### Answer 3
### Time complexity - O(N*M), Space complexity - O(M)
def canYouMake(s1: str, s2: str) -> int:
    n = len(s1)
    m = len(s2)

    prev = [0]*(m+1)

    for index1 in range(1,n+1):
        curr = [0]*(m+1)
        for index2 in range(1, m+1):
            if s1[index1-1] == s2[index2-1]:
                curr[index2] = 1 + prev[index2-1]
            else:
                curr[index2] = max(prev[index2], curr[index2-1])
        prev = curr[:]
    return n+m-(2*prev[m])
