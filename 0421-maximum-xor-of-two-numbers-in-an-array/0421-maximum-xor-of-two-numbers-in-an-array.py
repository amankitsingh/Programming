class Node:
    def __init__(self):
        self.links = []
    
    def contains_key(self, bit):
        return self.links[bit]!=NULL
    
    def get_bit(self, bit):
        return self.links[bit]
    
    def put_bit(self, bit, node):
        self.links[bit] = node
    
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        m, mask = 0, 0

        for i in range(32)[::-1]:
            mask |= 1 << i
            prefixes = {n & mask for n in nums}

            tmp = m | (1 << i)

            if any(prefix ^ tmp in prefixes for prefix in prefixes):
                m = tmp

        return m
        