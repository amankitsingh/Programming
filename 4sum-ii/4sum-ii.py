### Answer 1 - optimal approach
### TC - O(N^2), SC- O(N)
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

#Answer 2
def fourSumCount(self, A, B, C, D):
    AB = collections.Counter(a+b for a in A for b in B)
    return sum(AB[-c-d] for c in C for d in D)
