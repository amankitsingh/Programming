### Answer 1 - Recursion + Memoization
### Time complexity - O(N*N*N), Space complexity - O(N*N) + O(N)
class Solution:
    def minCut(self, string: str) -> int:
        if string ==  string[::-1]:
            return 0

        n = len(string)
        dp = [-1]*n

        def palipart(i):
            if i == n:
                return 0

            if dp[i]!= -1:
                return dp[i]

            mini = float("inf")
            for j in range(i,n):
                if string[i:j] == string[j:i:-1]:
                    mini = min(mini, 1 + palipart(j+1))
            dp[i] = mini
            return dp[i]
        return palipart(0)-1
        
### Answer 2 - Bottom-up approach
### Time complexity - O(N*N), Space complexity - O(N*N)
class Solution:
    def minCut(self, string: str) -> int:
        if string ==  string[::-1]:
            return 0

        n = len(string)
        dp = [0]*(n+1)

        for i in range(n-1,-1,-1):
            mini = float("inf")
            for j in range(i,n):    
                if string[i:j] == string[j:i:-1]:
                    mini = min(mini, 1 + dp[j+1])
            dp[i] = mini
        return dp[0]-1
