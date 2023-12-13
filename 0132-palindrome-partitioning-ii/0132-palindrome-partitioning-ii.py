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