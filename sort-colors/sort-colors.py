class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if nums[min_index] > nums[j]:
                    min_index = j
            nums[min_index],nums[i] = nums[i],nums[min_index]