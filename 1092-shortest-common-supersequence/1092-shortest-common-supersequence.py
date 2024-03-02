class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        n = len(s1)
        m = len(s2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for ind1 in range(1, n + 1):
            for ind2 in range(1, m + 1):
                if s1[ind1 - 1] == s2[ind2 - 1]:
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
                else:
                    dp[ind1][ind2] = 0+ max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])
        
        k = dp[n][m]
        i = n
        j = m
        result = ""
        while i > 0 and j > 0:
            if s1[i-1] == s2[j-1]:
                result+=s1[i-1]
                i-=1
                j-=1
            elif dp[i-1][j]> dp[i][j-1]:
                result+=s1[i-1]
                i-=1
            else:
                result+=s2[j-1]
                j-=1
        
        while i > 0:
            result+=s1[i-1]
            i-=1
        while j > 0:
            result+=s2[j-1]
            j-=1
        return result[::-1]
            
                
                