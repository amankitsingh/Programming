class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums)<2:
            return
        i,j= 0,1
        while j < len(nums):
            if nums[i] == 0 and nums[j] != 0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j+=1
            elif nums[i] != 0 and nums[j] == 0:
                i = j
                j+=1
            else:
                j+=1