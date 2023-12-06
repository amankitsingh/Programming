### Answer 1
### Time complexity - O(N*N+N), Space complexity - O(2N)~O(N)
class Solution:
    def findNumberOfLIS(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [1]*(n)
        count = dp[:]
        maxi = 1
        for i in range(1,n):
            for prev in range(i):
                if arr[i]>arr[prev] and dp[i] < 1 + dp[prev]:
                    dp[i] = 1 + dp[prev]
                    count[i] = count[prev]
                elif arr[i]>arr[prev] and dp[i] == 1 + dp[prev]:
                    count[i]+=count[prev]
            maxi = max(dp[i],maxi)

        result = 0
        for i in range(n):
            if dp[i] == maxi:
                result+=count[i]

        return result
