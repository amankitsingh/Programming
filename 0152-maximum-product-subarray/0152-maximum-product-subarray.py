class Solution:
    def maxProduct(self, arr: List[int]) -> int:
        n = len(arr)
        ans = float("-inf")
        prev,suff = 1,1
        for i in range(n):
            if prev == 0:
                prev = 1
            if suff == 0:
                suff = 1
            prev*=arr[i]
            suff*=arr[n-i-1]
            ans = max(ans, prev, suff)
        return ans