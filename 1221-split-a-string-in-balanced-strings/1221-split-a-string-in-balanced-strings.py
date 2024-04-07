### Answer 1 - keeping hash
### TC-O(n), SC - O(1)
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        sump = {"L":0,"R":0}
        result = 0
        for word in s:
            sump[word]+=1
            if sump["L"] == sump["R"]:
                result+=1
        return result

### Answer 2 - using 2 variable
### TC - O(n), SC - O(1)
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
