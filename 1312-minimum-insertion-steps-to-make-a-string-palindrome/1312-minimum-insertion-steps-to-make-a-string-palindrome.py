class Solution:
    def lps(self, s1,s2):
        n = len(s1)
        m = len(s2)
        dp = [[-1]*(m+1) for _ in range(n+1)]
        dp[0] = [0]*(m+1)
        for _ in range(n+1):
            dp[_][0] = 0
        for i in range(1,n+1):
            for j in range(1, m+1):
                dp[i][j] = 1 + dp[i-1][j-1] if s1[i-1] == s2[j-1] else max(dp[i-1][j], dp[i][j-1])
        return dp[n][m]
    def minInsertions(self, s: str) -> int:
        n = len(s)
        s2 = s[::-1]
        k = self.lps(s,s2)
        return n-k
        