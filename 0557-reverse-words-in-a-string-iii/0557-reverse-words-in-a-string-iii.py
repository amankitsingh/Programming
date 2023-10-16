class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        n = len(s)
        result = ""
        for c in range(n):
            if s[c]!=" ":
                stack.append(s[c])
            else:
                if stack:
                    while stack:
                        result+=stack.pop()
                    result+=" "
        if stack:
            while stack:
                    result+=stack.pop()
        else:
            result = result.slice(0,-1) if result[-1] == " " else result
        return result
        