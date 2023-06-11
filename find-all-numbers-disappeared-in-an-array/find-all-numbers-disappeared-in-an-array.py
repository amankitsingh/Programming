class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = len(nums)-1
        while i > 0:
            if nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i]= nums[i], nums[nums[i]-1]
            else:
                i-=1
        result = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                result.append(i+1)
        return result