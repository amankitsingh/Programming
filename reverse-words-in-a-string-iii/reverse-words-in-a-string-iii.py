class Solution:
    def reverseWords(self, s: str) -> str:
        result = s.split(" ")
        for i in range(len(result)):
            result[i] = "".join(reversed(result[i]))
        return " ".join(result)
            