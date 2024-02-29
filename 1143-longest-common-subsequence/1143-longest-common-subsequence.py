class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[-1]*m  for _ in range(n)]
        def lcs(ind1, ind2):
            if ind1<0 or ind2<0:
                return 0
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            
            if text1[ind1] == text2[ind2]:
                dp[ind1][ind2] = 1 + lcs(ind1-1,ind2-1)
            else:
                dp[ind1][ind2] = max(lcs(ind1-1,ind2),lcs(ind1,ind2-1))
            return dp[ind1][ind2]
        return lcs(n-1,m-1)