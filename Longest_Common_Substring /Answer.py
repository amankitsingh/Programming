### Answer 1
### Time complexity - O(N*M), Space complexity - O(N*M)
def lcs(str1: str, str2: str) -> int:
    n = len(str1)
    m = len(str2)
    dp = [[0]*(m+1) for _ in range(n+1)]

    maxi = float("-inf")
    for index1 in range(1, n+1):
        for index2 in range(1, m+1):
            if str1[index1-1] == str2[index2-1]:
                dp[index1][index2] = 1 + dp[index1-1][index2-1]
                maxi = max(maxi, dp[index1][index2])
    
    return maxi

### Answer 2
### Time complexity - O(N*M), Space complexity - O(N)
def lcs(str1: str, str2: str) -> int:
    n = len(str1)
    m = len(str2)
    prev = [0]*(m+1)

    maxi = float("-inf")
    for index1 in range(1, n+1):
        curr = [0]*(m+1)
        for index2 in range(1, m+1):
            if str1[index1-1] == str2[index2-1]:
                curr[index2] = 1 + prev[index2-1]
                maxi = max(maxi, curr[index2])
        prev = curr[:]
    
    return maxi
        
