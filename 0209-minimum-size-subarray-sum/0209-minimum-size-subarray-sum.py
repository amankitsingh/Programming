class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left,right,total,res=0,0,0,inf
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                res = min(res,right-left + 1)
                total-=nums[left]
                left+=1
            
        return res if res != inf else 0