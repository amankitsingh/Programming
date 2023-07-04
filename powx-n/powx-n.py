class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 1:
            return 1
        
        base = x
        result = 1
        temp_n = n
        n = abs(n) if n < 0 else n
        while n > 0:
            if n%2 == 1:
                result*=base
            base*=base
            n//=2
                
        return result if temp_n > 0 else 1/result 