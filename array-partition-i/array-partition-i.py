class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        i = 0
        result = []
        nums = sorted(nums)
        
        while i < len(nums):
            result.append([nums[i],nums[i+1]])
            i+=2
        output = 0
        
        for x in result:
            output+=min(x[0],x[1])
        return output