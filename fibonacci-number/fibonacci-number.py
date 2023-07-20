# Answer 1 - slow
class Solution:
    def fib(self, n: int) -> int:
        if n<2:
            return n
        return self.fib(n-1)+self.fib(n-2)

# Answer 2 - fast
class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        def helper(N):
            if N in cache:
                return cache[N]
            if N<2:
                result = N
            else:
                result = helper(N-1)+ helper(N-2)
            cache[N] = result
            return result
        return helper(n)
