class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumleft,sumright=0,sum(nums)
        
        for i in range(len(nums)):
            sumright-=nums[i]
            if sumleft==sumright:
                return i
            sumleft+=nums[i]
            
        return -1