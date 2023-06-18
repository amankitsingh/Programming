class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0
        for i in list(stones):
            if i in jewels:
                result+=1
        return result