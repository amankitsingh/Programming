from sortedcontainers import SortedSet

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max_array = SortedSet()
        for x in nums:
            if x in max_array:
                continue
            if len(max_array) == 3:
                max_array.add(x)
                max_array.discard(max_array[0])
            else:
                max_array.add(x)
        
        if len(max_array) == 3:
            return max_array[0]
        else:
            return max_array[-1]
            