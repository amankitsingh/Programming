class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j,iteration = 1,0,0
        if len(nums) <= 1:
            return len(nums)
        n = len(nums)
        
        while iteration<n:
            if i > len(nums)-1:
                break
            if nums[i] == nums[j]:
                del nums[i]
            else:
                j+=1
                i+=1
            iteration+=1
        return j+1
            