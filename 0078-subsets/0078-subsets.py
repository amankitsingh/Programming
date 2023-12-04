### Time complexity - O(N*N), Space complexity - O(2*N)
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

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        subset = []
        def combi(start, comb, k):
            if len(comb) == k:
                subset.append(comb[:])
                return
            
            for i in range(start, n+1):
                comb.append(nums[start])
                backtrack(i+1, comb, k)
                comb.pop()
            
        for k in range(2, n):
            combi(1, [], k)
