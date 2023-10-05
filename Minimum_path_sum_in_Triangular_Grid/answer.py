### Answer 1 - top down approach
### Time complexity - O(N*M) , space complexity - O(M-1)+O(N-1)+O(M*N)
def minimumPathSum(triangle, n):
    dp = [[-1 for j in range(n)] for i in range(n)]
    def findpath(i,j,dp):
        if dp[i][j]!=-1:
            return dp[i][j]
        if i == n-1:
            return triangle[i][j]

        down = triangle[i][j] + findpath(i+1,j,dp)
        diagonal = triangle[i][j] + findpath(i+1,j+1,dp)
        dp[i][j] =  min(down,diagonal)
        return dp[i][j]
         
    return findpath(0,0,dp)
  
### Answer 2 - bottom up approach
### Time complexity - O(N*M) , space complexity - O(M)
def minimumPathSum(triangle, n):
    dp = [[-1 for j in range(n)] for i in range(n)]
    for i in range(n):
        dp[n-1][i] = triangle[n-1][i]
    
    for i in range(n-2,-1,-1):
        for j in range(i,-1,-1):
            down = triangle[i][j] + dp[i+1][j]
            diagonal = triangle[i][j] + dp[i+1][j+1]
            dp[i][j] = min(down,diagonal)
    return dp[0][0]

### Answer 2 - bottom up approach
### Time complexity - O(N*(N+1)) , space complexity - O(M)
def minimumPathSum(triangle, n):
  front = [0] * n
  for j in range(n):
      front[j] = triangle[n - 1][j]
  for i in range(n - 2, -1, -1):
      for j in range(i + 1):
          front[j] = triangle[i][j] + min(front[j], front[j + 1])
  return front[0]
