class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = Counter(nums1)
        
        result = []
        for x in nums2:
            if c[x] > 0:
                result.append(x)
                c[x] -=1
        return result