### Answer - Concept of prefix sum
### If we take the sum of the subarray and subtract the k from it, we are left(x-k) with k
### Time complexity - O(N), Space complexity - O(N)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result_map = defaultdict(int)
        result_map[0]=1
        n = len(nums)
        prevSum = 0
        cnt = 0
        for i in range(n):
            prevSum += nums[i]
            remove = prevSum-k
            cnt+=result_map[remove]
            result_map[prevSum]+=1
        return cnt
