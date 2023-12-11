### Answer 1
### Time complexity - O(N*N*N), Space complexity - O(N*N) +O(N)
class Solution:
    def maxCoins(self, arr: List[int]) -> int:
        n = len(arr)
        arr = [1] + arr + [1]
        dp = [[-1]*(n+2) for _ in range(n+2)]
        def maxcoin(i,j):
            if i>j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            maxi = float("-inf")
            for k in range(i,j+1):
                maxi = max(maxi,maxcoin(i,k-1) + maxcoin(k+1,j) + arr[i-1]*arr[k]*arr[j+1])
            dp[i][j] = maxi
            return maxi
        return maxcoin(1,n)

### Answer 2
### Time complexity - O(N*N*N), Space complexity - O(N*N)
class Solution:
    def maxCoins(self, arr: List[int]) -> int:
        n = len(arr)
        arr = [1] + arr + [1]
        dp = [[0]*(n+2) for _ in range(n+2)]

        for i in range(n,0,-1):
            for j in range(1,n+1):
                if i > j:
                    continue
                maxi = float("-inf")
                for k in range(i,j+1):
                    maxi = max(maxi,dp[i][k-1] + dp[k+1][j] + arr[i-1]*arr[k]*arr[j+1])
                dp[i][j] = maxi
        return dp[1][n]
