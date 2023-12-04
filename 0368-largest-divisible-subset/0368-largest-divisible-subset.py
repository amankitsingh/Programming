class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums)<2:
            return nums
        n = len(nums)
        lastIndex = -1
        nums.sort()
        dp = [1]*n
        temp = list(range(n))
        maxi = -1
        for curr in range(1,n):
            for prev in range(curr-1,-1,-1):
                if nums[curr]%nums[prev] == 0 and 1+dp[prev] > dp[curr]:
                    dp[curr] = 1+dp[prev]
                    temp[curr] = prev
                
                if dp[curr] > maxi:
                    maxi = dp[curr]
                    lastIndex = curr
        
        
        result = [nums[lastIndex]]
        while temp[lastIndex]!=lastIndex:
            lastIndex = temp[lastIndex]
            result.append(nums[lastIndex])
        
        result.reverse()
        return result
        
                    