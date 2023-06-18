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

#Answer 2
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        # O(1) time 
        if k == len(nums):
            return nums
        
        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)   
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get) 
