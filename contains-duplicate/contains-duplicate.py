class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for x in nums:
            if x in visited:
                return True
            visited.add(x)
        
        return False