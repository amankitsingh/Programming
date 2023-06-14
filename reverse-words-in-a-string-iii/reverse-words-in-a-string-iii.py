class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join((i[::-1] for i in s.split()))
        
#Answer 2
class Solution:
    def reverseWords(self, s: str) -> str:
        result = s.split(" ")
        for i in range(len(result)):
            result[i] = "".join(reversed(result[i]))
        return " ".join(result)
            
