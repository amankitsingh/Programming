### Answer 1
### Time complexity - O(N*N), Space complexity - O(N*N) + O(N)
### this will not work for larger cases
def longestIncreasingSubsequence(arr, n) :
    dp = [[-1]*(n+1) for _ in range(n+1)]
    def lcs(index, prev_index):

        if index == n:
            return 0

        if dp[index][prev_index+1] != -1:
            return dp[index][prev_index+1]

        pick = 0
        nonpick = 0 + lcs(index+1, prev_index)
        if prev_index == -1 or arr[index] > arr[prev_index]:
            pick = 1 + lcs(index+1, index)
        dp[index][prev_index+1] = max(pick,nonpick)
        return dp[index][prev_index+1]
    return lcs(0,-1)

### Answer 2
### Time complexity - O(N*N), space complexity - O(N*N)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp = [[0]*(n+1) for _ in range(n+1)]
        
        
        for index in range(n-1,-1,-1):
            for prev_index in range(index-1, -2,-1):                
                nonpick = 0 + dp[index+1][prev_index+1]
                pick = 0
                if prev_index == -1 or nums[index] > nums[prev_index]:
                    pick = 1 + dp[index+1][index+1]
            
                dp[index][prev_index+1] = max(pick,nonpick)
        return dp[0][0]

### Answer 3
### Time complexity - O(NlogN), Space complexity-  O(N)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        def binary_search(nums,n):
            l = 1
            temp = [nums[0]]
            for i in range(1,n):
                if nums[i] > temp[-1]:
                    temp.append(nums[i])
                    l += 1
                else:
                    def lower_bound(temp,nums):
                        l,r = 0,len(temp)-1
                        while l<=r:
                            mid = (l+r)//2
                            if temp[mid] >= nums:
                                res = mid
                                r = mid - 1
                            elif temp[mid] < nums:
                                l = mid + 1
                        return res

                    idx = lower_bound(temp,nums[i])
                    temp[idx] = nums[i]

            return l
        return binary_search(nums,n)
