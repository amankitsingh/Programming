class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        for x in nums1:
            if x in nums2:
                result.add(x)
        return result