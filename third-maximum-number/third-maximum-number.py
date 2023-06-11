class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        firmax = -inf
        secmax = -inf
        thrmax = -inf
        
        for x in nums:
            if x == firmax or x == secmax or x == thrmax:
                continue
                
            if x > firmax:
                thrmax,secmax = secmax,thrmax
                secmax,firmax = firmax,x
            elif x > secmax:
                thrmax,secmax = secmax,x
            elif x > thrmax:
                thrmax = x
        
        if thrmax == -inf:
            return firmax
        return thrmax