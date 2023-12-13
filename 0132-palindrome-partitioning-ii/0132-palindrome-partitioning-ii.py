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