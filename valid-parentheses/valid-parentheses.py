class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_paran = {"(":")", "[":"]","{":"}"}
        for i in s:
            if i in valid_paran:
                stack.append(i)
            elif i in valid_paran.values():
                if not stack or (i != valid_paran[stack.pop()]):
                    return False
        
        return True if not stack else False