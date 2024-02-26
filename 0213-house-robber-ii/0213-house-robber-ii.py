class Solution:
    def solve(self, arr):
        prev2 = 0
        prev = arr[0]
        for i in range(1,self.n-1):
            pick = arr[i]
            if i > 1:
                pick +=prev2
            nonpick = 0 + prev
            curr = max(nonpick,pick)
            prev2 = prev
            prev = curr
        return prev
    def rob(self, nums: List[int]) -> int:
        self.n = len(nums)
        if self.n == 0:
            return 0
        if self.n == 1:
            return nums[0]
        
        self.arr1 = nums[1:]
        self.arr2 = nums[0:self.n-1]
        return max(self.solve(self.arr1),self.solve(self.arr2))
        