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