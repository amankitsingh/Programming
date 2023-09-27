
### Anwer 1 - top down approach using dp(recursive and store in array)
#### Time complexity - O(n), Space Complexity - O(n)+ O(n) ~ O(n)

class Solution:
    def subsequence(self, nums):
        dp = [-1]*len(nums)
        def findF(index, arr, dp):
            if dp[index] != -1:
                return dp[index]
            if index == 0:
                return arr[0]
            if index < 0:
                return 0
            pick = arr[index] + findF(index-2, arr, dp)
            nonpick = 0 + findF(index-1, arr, dp)
            dp[index] = max(pick, nonpick)
            return dp[index]
        findF(len(nums)-1, nums, dp)
        return dp[-1]
Solution().subsequence([1,2,3,1,3,5,8,1,9])

### Answer 2 - bottom up approach using dp (iterative)
#### Time complexity - O(n), Space Complexity - O(n)

class Solution:
    def subsequence(self, nums):
        dp = [-1]*len(nums)
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            pick = nums[i]
        
            if i > 1:
                pick += dp[i-2]
            nonpick = 0 + dp[i-1]
            dp[i] = max(pick, nonpick)
        return dp[-1]
Solution().subsequence([1,2,3,1,3,5,8,1,9])

### Answer 3 - bottom up approach using 2 pointers to space optimize the solution (iterative)
#### Time complexity - O(n), Space Complexity - O(1)

class Solution:
    def subsequence(self, nums):
        prev2 = 0
        prev = nums[0]
        
        for i in range(1, len(nums)):
            pick = nums[i]
            
            if i > 1:
                pick+=prev2
            nonpick = 0 + prev
            curr = max(pick,nonpick)
            prev2 = prev
            prev = curr
        return prev
Solution().subsequence([2,1,4,9])        
Solution().subsequence([1,2,3,1,3,5,8,1,9])
