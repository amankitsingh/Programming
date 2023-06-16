class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = Counter(nums1)
        
        result = []
        for x in nums2:
            if c.get(x,0) > 0:
                result.append(x)
                c[x] -=1
        return result
    
# Answer 2
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for x in range(len(nums2)):
            if nums2[x] in nums1:
                result.append(nums2[x])
                nums1[nums1.index(nums2[x])] = -1
        return result
