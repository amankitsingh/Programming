# Answer 1 - Newton method
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        r = num
        while r*r > num:
            r = (r + num/r)//2
        return r*r == num
        
# Answer 2 - Binary Search        
class Solution:
    def isPerfectSquare(self, num):
        l, h = 1, int(num/2)
        while l<h:
            mid = (l+h)>>1
            if mid*mid==num:return True
            if mid*mid>num:h = mid-1
            else:l = mid+1
        return l*l==num
