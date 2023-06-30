class Solution:
    def mySqrt(self, x: int) -> int:
        if x ==1:return 1
        left,right = 1, x//2
        
        while left < right and left+1!=right:
            mid = (left+right)//2
            square = pow(mid,2)
            if square > x:
                right = mid-1
            elif square < x:
                left = mid
            else:
                return mid
            
            if left == right:
                return left
        if pow(left,2) <= x < pow(right,2):
            return left
        else:
            return right