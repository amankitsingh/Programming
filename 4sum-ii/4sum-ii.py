class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dic = collections.defaultdict(int)
        for n1 in nums1:
            for n2 in nums2:
                temp = -(n1+n2)
                dic[temp]+=1
                
        result = 0
        for n3 in nums3:
            for n4 in nums4:
                result += dic[n3+n4]
        return result
        