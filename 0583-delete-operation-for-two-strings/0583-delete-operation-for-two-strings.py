class Solution:
    def lcs(self, ind1, ind2,dp):
        if ind1 <0 or ind2 < 0:
            return 0
        if dp[ind1][ind2]!=-1:
            return dp[ind1][ind2]
        if self.s1[ind1] == self.s2[ind2]:
            dp[ind1][ind2] = 1 + self.lcs(ind1-1,ind2-1,dp)
        else:
            dp[ind1][ind2] = max(self.lcs(ind1-1,ind2,dp),self.lcs(ind1,ind2-1,dp))
        return dp[ind1][ind2]
        
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        self.s1 = word1
        self.s2 = word2
        dp = [[-1]*(m+1) for _ in range(n+1)]
        return n+m - (2*self.lcs(n-1,m-1,dp))