class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0]*(n+1)
        for i in range(n-1,-1,-1):
            maxi,length,maxElement = float("-inf"),0,float("-inf")
            for j in range(i, min(i+k,n)):
                length+=1
                maxElement = max(arr[j], maxElement)
                sump = maxElement*length + dp[j+1]
                maxi = max(maxi,sump)
            dp[i] = maxi    
        return dp[0]