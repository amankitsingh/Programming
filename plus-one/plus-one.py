class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for x in digits:
            s+=str(x)
        number = int(s) + 1
        return [int(x) for x in str(number)]
        