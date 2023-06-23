class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        counter = collections.Counter({0:1})
        for i in nums:
            step = collections.Counter()
            for j in counter:
                step[j+i] += counter[j]
                step[j-i] += counter[j]
            counter = step
        return counter[target]