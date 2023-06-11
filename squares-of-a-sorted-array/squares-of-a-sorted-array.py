class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l,r,n = 0, len(nums)-1, len(nums)
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i]*=-1
                
        result = [0] * n
        n-=1
        while n >= 0:
            if nums[l] > nums[r]:
                result[n] = nums[l]
                l+=1
            else:
                result[n] = nums[r]
                r-=1
            n-=1
        
        for i in range(len(result)):
            result[i]*=result[i]
        return result