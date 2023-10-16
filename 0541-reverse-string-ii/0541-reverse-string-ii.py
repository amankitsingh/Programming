class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        size = len(s)
        for i in range(0,size,2*k):
            s[i:i+k] = s[i:i+k][::-1]
        return "".join(s)