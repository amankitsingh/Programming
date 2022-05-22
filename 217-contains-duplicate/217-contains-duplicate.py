class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_ = set()
        for x in nums:
            if x in set_:
                return True
            set_.add(x)
        
        return False