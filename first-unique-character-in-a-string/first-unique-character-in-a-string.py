class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = Counter(s)
        for key,value in d.items():
            if value ==1:
                return s.index(key)
        return -1
            