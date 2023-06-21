class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_paran = {"(":")", "[":"]","{":"}"}
        for i in s:
            if i in valid_paran.keys():
                stack.append(i)
            elif i in valid_paran.values():
                if not stack:
                    return False
                if (stack and i != valid_paran[stack.pop()]):
                    return False
        
        return True if not stack else False