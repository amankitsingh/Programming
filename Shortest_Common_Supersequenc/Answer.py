### Answer 1
### Time complexity - O(N*M), Space complexity - O(N*M)
def shortestSupersequence(a: str, b: str) -> str:
    n = len(a)
    m = len(b)

    dp = [[-1]*(m+1) for _ in range(n+1)]

    for ind1 in range(1, n + 1):
        for ind2 in range(1, m + 1):
            if a[ind1 - 1] == b[ind2 - 1]:
                dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
            else:
                dp[ind1][ind2] = 0+ max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])
    i=n
    j=m
    ans = ""
    while i >0 and j>0:
        if a[i-1] == b[j-1]:
            ans+=a[i-1]
            i-=1
            j-=1
        elif dp[i-1][j] > dp[i][j-1]:
            ans+=a[i-1]
            i-=1
        else:
            ans+=b[j-1]
            j-=1
    
    while i>0:
        ans+=a[i-1]
        i-=1
    
    while j>0:
        ans+=b[j-1]
        j-=1
    
    return ans[::-1]
    

    
