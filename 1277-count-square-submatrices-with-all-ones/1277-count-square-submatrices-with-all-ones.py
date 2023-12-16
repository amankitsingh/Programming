### Answer 1
### Time complexity - O(N*M + 3*N + M)~O(N*M), Space complexity -  O(N*M)
### Intuition is to check the right end of the square (dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
class Solution:
    def countSquares(self, arr: List[List[int]]) -> int:
        n = len(arr)
        m = len(arr[0])
        dp = [[0]*m for _ in range(n)]
        for i in range(m): dp[0][i] = arr[0][i]
        for j in range(n): dp[j][0] = arr[j][0]

        for i in range(1,n):
            for j in range(1,m):
                if arr[i][j] == 1:
                    dp[i][j] = 1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])

        result=0
        for i in dp:
            result+=sum(i)
        return result
