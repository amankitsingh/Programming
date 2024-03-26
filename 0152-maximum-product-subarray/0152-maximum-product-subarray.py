### Answer 1 - Brute force
### TC - O(n^3), SC-O(1)
class Solution:
    def maxProduct(self, arr: List[int]) -> int:
        result = float('-inf')
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                prod = 1
                for k in range(i, j + 1):
                    prod *= nums[k]
                result = max(result, prod)
        return result

### Answer 2 - Better than brute force
### TC - O(n^2), SC-O(1)
class Solution:
    def maxProduct(self, arr: List[int]) -> int:
        n = len(arr)
        ans = arr[0]
        for i in range(n):
            prod = arr[i]
            for j in range(i+1,n):
                ans = max(ans, prod)
                prod*=arr[j]
            ans = max(ans, prod)
        return ans

### Answer 3 - Optimal solution
### TC - O(n), SC-O(1)
### intuition - if 0 then the product becomes 0, if odd -ve number then ans is -ve, if even -ve then ans is +ve
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
