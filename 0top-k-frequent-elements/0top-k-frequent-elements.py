class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = collections.Counter(nums)
        result = []
        maxvalue = 0
        hashmap = sorted(hashmap.items(), key = lambda kp:(kp[1], kp[0]))
        for i in range(len(hashmap)-1,-1,-1):
            if k > 0:
                result.append(hashmap[i][0])
                k-=1
            else:
                break
        return result