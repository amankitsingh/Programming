class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        result = 0
        for word in s:
            if word == "R":
                balance+=1
            elif word == "L":
                balance-=1
            if balance ==0:
                result+=1
        return result