class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxIndex = -1
        maxElement = 0
        for i in range(len(nums)):
            if maxElement < nums[i]:
                maxIndex=i
                maxElement = nums[i]
        for x in nums:
            if x!=maxElement and maxElement < 2*x:
                return -1
        
        return maxIndex
        
        