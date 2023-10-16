class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        result = ""
        i= 0
        temp_n = n
        while i < n:
            if k <= temp_n < 2*k:
                end = i+k
                temp = ""
                while i<end:
                    temp+=s[i]
                    i+=1
                result+=temp[::-1]
                while i < n:
                    result+=s[i]
                    i+=1
            elif temp_n < k:
                end = n
                temp = ""
                while i<end:
                    temp+=s[i]
                    i+=1
                result+=temp[::-1]
            else:
                end = i+k
                temp = ""
                while i<end:
                    temp+=s[i]
                    i+=1
                result+=temp[::-1]
                while i<end+k:
                    result+=s[i]
                    i+=1
                temp_n-=2*k
        return result