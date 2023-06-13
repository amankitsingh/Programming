class Solution:
    def reverseString(self, s: List[str]) -> None:
        j = len(s)-1
        
        for i in range(int(len(s)/2)):
            s[i],s[j] = s[j],s[i]
            j-=1
        return s