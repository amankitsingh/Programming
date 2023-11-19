class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        
        dp =[[0]*(m+1) for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][0] = i
        
        for j in range(m+1):
            dp[0][j] = j
        
        for index1 in range(1, n+1):
            for index2 in range(1, m+1):
                if word1[index1-1] == word2[index2-1]:
                    dp[index1][index2] = dp[index1-1][index2-1]
                else:
                    dp[index1][index2] = 1 + min(dp[index1-1][index2],min(dp[index1-1][index2-1],
                                                                            dp[index1][index2-1]))
        
                                            
                                             
        return dp[n][m]