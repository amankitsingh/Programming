### Answer 1 - using 2 pointer
### Time complexity - O(N), space complexity - o(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        currentsum = 0
        for num in nums:
            if currentsum < 0:
                currentsum = 0
            currentsum+=num
            maxsum = max(maxsum,currentsum)
            
        return maxsum

### Answer 2 - using dp
### Time complexity - O(N), space complexity - O(N)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        ans = dp[0]
        
        for i in range(1, n):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
            ans = max(ans,dp[i])
        return ans
