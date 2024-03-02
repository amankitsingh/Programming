class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        dp = [[-1]*(m+1) for _ in range(n+1)]
        def nd(ind1, ind2):
            if ind2 < 0:
                return 1
            if ind1 < 0:
                return 0
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            if s[ind1] == t[ind2]:
                dp[ind1][ind2] = nd(ind1-1,ind2) + nd(ind1-1,ind2-1)
            else:
                dp[ind1][ind2] = nd(ind1-1,ind2)
            return dp[ind1][ind2]
        return nd(n-1,m-1)