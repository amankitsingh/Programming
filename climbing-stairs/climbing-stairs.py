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