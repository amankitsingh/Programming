class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for x in nums:
            iteration = 0
            while x>0:
                iteration+=1
                x = int(x/10)
            if iteration % 2 == 0:
                result+=1
        return result