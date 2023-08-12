# Answer 1 - Time complexity O(n), Space complexity O(n)
import sys
import math

def solve(ind, height, dp):
    if ind == 0:
        return 0
    if dp[ind] != -1:
        return dp[ind]
    jumpTwo = sys.maxsize
    jumpOne = solve(ind-1, height, dp) + abs(height[ind] - height[ind-1])
    if ind > 1:
        jumpTwo = solve(ind-2, height, dp) + abs(height[ind] - height[ind-2])
    dp[ind] = min(jumpOne, jumpTwo)
    return dp[ind]

if __name__ == "__main__":
    height = [30, 10, 60, 10, 60, 50]
    n = len(height)
    dp = [-1] * n
    print(solve(n-1, height, dp))
