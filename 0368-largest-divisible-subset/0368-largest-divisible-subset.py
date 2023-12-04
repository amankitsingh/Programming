### Answer 1
### Time complexity - O(n*n), space complexity - O(2*n)
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
        
### Answer 2 - same as above
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dp = [1]*n
        temp = [-1]*n
        maxi = 0
        for curr in range(1,n):
            for prev in range(curr):
                if nums[curr]%nums[prev] == 0 and 1+dp[prev] > dp[curr]:
                    dp[curr] = 1+dp[prev]
                    temp[curr] = prev
                
                if dp[curr] > dp[maxi]:
                    maxi = curr
        
        result = []
        while maxi >= 0:
            result.append(nums[maxi])
            maxi = temp[maxi]
        
        return result
