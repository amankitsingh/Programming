class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp = [[0]*(n+1) for _ in range(n+1)]
        
        
        for index in range(n-1,-1,-1):
            for prev_index in range(index-1, -2,-1):                
                nonpick = 0 + dp[index+1][prev_index+1]
                pick = 0
                if prev_index == -1 or nums[index] > nums[prev_index]:
                    pick = 1 + dp[index+1][index+1]
            
                dp[index][prev_index+1] = max(pick,nonpick)
        return dp[0][0]