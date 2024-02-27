class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        dp = [[-1 for _ in range(N)] for _ in range(N)]
        def unpath(i,j):
            if i==N-1:
                return triangle[i][j]
            if dp[i][j]!=-1:
                return dp[i][j]
            down = triangle[i][j] + unpath(i+1,j)
            diagonal = triangle[i][j] + unpath(i+1,j+1)
            dp[i][j] =  min(down,diagonal)
            return dp[i][j]
        return unpath(0,0)