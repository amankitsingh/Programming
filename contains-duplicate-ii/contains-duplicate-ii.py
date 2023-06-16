class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}
        for i,value in enumerate(nums):
            if value in last_seen and i - last_seen[value] <= k:
                return True
            last_seen[value] = i
        return False