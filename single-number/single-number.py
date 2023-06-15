class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bit_wise_add = 0
        for x in nums:
            bit_wise_add ^= x
        
        return bit_wise_add