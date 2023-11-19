### Answer 1
### Time complexity - O(N*M), Space complexity - O(N*M) +O(N+M)
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

### Answer 2
### Time complexity - O(N*M), Space complexity - O(N*M)
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


### Answer 3
### Time complexity - O(N*M), Space complexity - O(N*M)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        
        prev = [j for j in range(m + 1)]
        
        for index1 in range(1, n+1):
            curr = [0]*(m+1)
            curr[0] = index1
            for index2 in range(1, m+1):
                if word1[index1-1] == word2[index2-1]:
                    curr[index2] = prev[index2-1]
                else:
                    curr[index2] = 1 + min(prev[index2],min(prev[index2-1],curr[index2-1]))
            #prev,curr = curr,prev
            prev = curr[:]
                                            
                                             
        return prev[m]
