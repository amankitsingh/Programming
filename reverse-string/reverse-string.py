# Answer 1 - Iterative
class Solution:
    def reverseString(self, s: List[str]) -> None:
        j = len(s)-1
        
        for i in range(int(len(s)/2)):
            s[i],s[j] = s[j],s[i]
            j-=1
        return s
# Answer 2 - Recursive
class Solution:
    def reverseString(self, s: List[str]) -> None:
        def helper(low,high):
            if low>high:
                return
            s[low],s[high]=s[high],s[low]
            helper(low+1,high-1)
        helper(0,len(s)-1)
        
        
