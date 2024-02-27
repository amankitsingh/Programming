class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        front = [0]*N
        curr = [0]*N
        for i in range(N):
            front[i] = triangle[N-1][i]
        
        for i in range(N-2,-1,-1):
            for j in range(i,-1,-1):
                down = triangle[i][j] + front[j]
                diagonal = triangle[i][j] + front[j+1]
                curr[j] =  min(down,diagonal)
            front = curr[::]
        
        return front[0]