class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = collections.Counter(nums)
        result = []
        maxvalue = 0
        hashmap = sorted(hashmap.items(), key=lambda k:k[1])
        return [i for i,b in hashmap[len(hashmap)-k:]]
        