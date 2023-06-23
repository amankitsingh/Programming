class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i,j,carry,result = len(a)-1,len(b)-1, 0, ""
        while i>=0 or j>=0:
            sump = carry
            if i >=0: sump += ord(a[i]) - ord('0')
            if j >=0: sump += ord(b[j]) - ord('0')
            i,j = i-1,j-1
            result += str(sump%2)
            carry = 1 if sump > 1 else 0
        if carry: result+=str(carry)
        return result[::-1]
