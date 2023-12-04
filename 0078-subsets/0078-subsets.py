class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subset = []
        def backtrack(start, comb, k):
            if len(comb) == k:
                subset.append(comb[:])
                return
            
            for i in range(start, n):
                comb.append(nums[i])
                backtrack(i+1, comb, k)
                comb.pop()
            
        for k in range(n+1):
            backtrack(0, [], k)
        return subset