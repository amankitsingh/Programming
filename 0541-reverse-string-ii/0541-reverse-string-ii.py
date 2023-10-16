class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse(i,j):
            j = min(j,size-1)
            while i<j:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
        s = list(s)
        size = len(s)
        for i in range(0,size, 2*k):
            reverse(i, i+k-1)
        return "".join(s)