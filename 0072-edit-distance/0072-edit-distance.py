class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        
        dp =[[-1]*(m+1) for _ in range(n+1)]
        
        def helper(index1, index2):
            if index1 < 0:
                return index2+1
            if index2 < 0:
                return index1+1
            
            if dp[index1][index2] != -1:
                return dp[index1][index2]
            
            if word1[index1] == word2[index2]:
                dp[index1][index2] = helper(index1-1,index2-1)
            else:
                dp[index1][index2] = 1 + min(helper(index1-1,index2),min(helper(index1-1,index2-1),
                                                                        helper(index1,index2-1)))
            return dp[index1][index2]
        
                                            
                                             
        return helper(n-1,m-1)