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