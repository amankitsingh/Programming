class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totSum = sum(nums)
        if totSum%2 == 1:
            return False
        else:
            k = totSum//2
            n = len(nums)
            prev = [False]*(k+1)
            prev[0] = True
            
            if nums[0] <= k:
                prev[nums[0]] = True
                
            for ind in range(1,n):
                curr = [False]*(k+1)
                curr[0] = True
                
                for target in range(1, k+1):
                    nonPick = prev[target]
                    pick = False
                    if nums[ind] <= target:
                        pick = prev[target-nums[ind]]
                    curr[target] = pick or nonPick
                prev = curr
        return prev[k]