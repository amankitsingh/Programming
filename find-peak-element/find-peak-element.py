class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)<=3:
            max_index = (0,nums[0])
            for i in range(len(nums)):
                if nums[i] > max_index[1]:
                    max_index = (i, nums[i])
            return max_index[0]
        
        for i in range(len(nums)):
            if i != 0 and i != len(nums)-1:
                if (nums[i] > nums[i-1]) and (nums[i] > nums[i+1]):
                    return i
               
        return len(nums)-1 if nums[-1] > nums[-2] else 0 