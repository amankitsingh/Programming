class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for x in range(len(nums2)):
            if nums2[x] in nums1:
                result.append(nums2[x])
                nums1[nums1.index(nums2[x])] = -1
        return result