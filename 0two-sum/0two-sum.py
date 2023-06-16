class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hashmap and hashmap[comp]!=i:
                return [i,hashmap[comp]]