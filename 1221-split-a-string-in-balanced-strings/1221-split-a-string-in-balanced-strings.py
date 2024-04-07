class Solution:
    def balancedStringSplit(self, s: str) -> int:
        sump = {"L":0,"R":0}
        result = 0
        for word in s:
            sump[word]+=1
            if sump["L"] == sump["R"]:
                result+=1
        return result