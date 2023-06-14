class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left,right,sumofsubarray,res=0,0,0,inf
        for right in range(len(nums)):
            sumofsubarray += nums[right]
            while sumofsubarray >= target:
                res = min(res,right-left + 1)
                sumofsubarray-=nums[left]
                left+=1
            
        return res if res != inf else 0