# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        first = 1
        last = n
        badversion = 0
        while first<last:
            mid = first+(last-first)//2 # Solution for most famous overflow bug, if used (first+last)/2
            # or this can be usedmid = (first + last) >> 1;
            if first==mid or last==mid:
                break
            if isBadVersion(mid):
                badversion = mid
                last = mid
            else:
                first = mid
        if isBadVersion(first):
            return first 
        elif isBadVersion(last):
            return last
        else:
            badversion
            
