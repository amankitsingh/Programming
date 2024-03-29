# Recursive
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def helper(N):
            if N in cache:
                return cache[N]
            if N<=3:
                result = N
            else:
                result = helper(N-1)+ helper(N-2)
            cache[N] = result
            return result
        return helper(n)

# Recursive
class Solution:
    memo = {}
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = self.climbStairs(n-1)+self.climbStairs(n-2)
        return self.memo[n]

# Iterative
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1,2:2}
        for i in range(3,n+1):
            memo[i] = memo[i-1]+memo[i-2]
        return memo[n]
