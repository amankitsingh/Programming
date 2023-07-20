# Answer1 - Iterative
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

# Answer 2 - Recursive
class Solution:
    def binaryExp(self, x: float, n: int) -> float:
        # Base case, to stop recursive calls.
        if n == 0:
            return 1
        if n < 0:
            return 1.0 / self.binaryExp(x, -1 * n)
       
        # Perform Binary Exponentiation.
        # If 'n' is odd we perform Binary Exponentiation on 'n - 1' and multiply result with 'x'.
        if n % 2 == 1:
            return x * self.binaryExp(x * x, (n - 1) // 2)
        # Otherwise we calculate result by performing Binary Exponentiation on 'n'.
        else:
            return self.binaryExp(x * x, n // 2)

    def myPow(self, x: float, n: int) -> float:
        return self.binaryExp(x, n)
