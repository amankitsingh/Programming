
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
