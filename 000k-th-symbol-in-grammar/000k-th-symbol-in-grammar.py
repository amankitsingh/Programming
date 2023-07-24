class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return bin(k-1).count('1')%2


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return k - 1
        half = 1<<(n-2)
        if k <= half:
            return self.kthGrammar(n-1, k)
        else:
            return int(not self.kthGrammar(n-1, k - half))  
