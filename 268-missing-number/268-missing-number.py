class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n not in nums:
            return n
        for x in range(n):
            if x not in nums:
                return x