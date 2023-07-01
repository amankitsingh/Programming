class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
        mid = len(nums)//2
        for i in range(mid+1):
            if nums[i] == target:
                return i
        for i in range(mid+1,len(nums)):
            if nums[i] == target:
                return i
        
        return -1