### Answer 1 - memorization approach
### Time complexity - O(N*M*M)*9, space complexity - O(N) + O(N*M*M) ~ O(N*M*M)
def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:
    dp = [[[-1 for i in range(c)] for j in range(c)] for k in range(r)]
    def find_max_chocolate(i, j1, j2):
        if ( j1 < 0 or j1 >= c) or (j2 < 0 or j2 >= c):
            return float("-inf")
        if dp[i][j1][j2]!=-1:
            return dp[i][j1][j2]
        if i == r-1:
            if j1 == j2:
                return grid[i][j1]
            else:
                return grid[i][j1] + grid[i][j2]
        
        maxi = float("-inf")
        for di in range(-1, 2):
            for dj in range(-1,2):
                ans = 0
                if j1 == j2:
                    ans = grid[i][j1] + find_max_chocolate(i+1,j1+di,j2+dj)
                else:
                    ans = grid[i][j1] + grid[i][j2]+ find_max_chocolate(i+1,j1+di,j2+dj)
                maxi = max(maxi, ans)
        dp[i][j1][j2] = maxi
        return dp[i][j1][j2]
    return find_max_chocolate(0, 0, c-1)

### Answer 2 - tabulization approach
### Time complexity - O(N*M*M)*9, space complexity - O(N*M*M)
def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:
    dp = [[[0 for i in range(c)] for j in range(c)] for k in range(r)]
    for j1 in range(c):
        for j2 in range(c):
            if j1 == j2:
                dp[r-1][j1][j2] = grid[r-1][j1]
            else:
                dp[r-1][j1][j2] = grid[r-1][j1] + grid[r-1][j2]
    
    for i in range(r-2, -1, -1):
        for j1 in range(c):
            for j2 in range(c):
                maxi = float("-inf")
                for di in range(-1, 2):
                    for dj in range(-1,2):
                        ans = 0
                        if j1 == j2:
                            ans = grid[i][j1]
                        else:
                            ans = grid[i][j1] + grid[i][j2]                            
                        if (j1+di) < 0 or (j1+di) >= c or (j2+dj) < 0 or (j2+dj) >=c:
                            ans += float("-inf")
                        else:
                            ans += dp[i+1][j1+di][j2+dj]
                        maxi = max(maxi, ans)
                dp[i][j1][j2] = maxi
    return dp[0][0][c-1]

### Answer 3 - tabulization approach with space optimized
### Time complexity - O(N*M*M)*9, space complexity - O(M*M)
def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:
  front = [[0] * c for _ in range(c)]
  cur = [[0] * c for _ in range(c)]
  for j1 in range(c):
      for j2 in range(c):
          if j1 == j2:
              front[j1][j2] = grid[r-1][j1]
          else:
              front[j1][j2] = grid[r-1][j1] + grid[r-1][j2]
  
  for i in range(r-2, -1, -1):
      for j1 in range(c):
          for j2 in range(c):
              maxi = float("-inf")
              for di in range(-1, 2):
                  for dj in range(-1,2):
                      ans = 0
                      if j1 == j2:
                          ans = grid[i][j1]
                      else:
                          ans = grid[i][j1] + grid[i][j2]                            
                      if (j1+di) < 0 or (j1+di) >= c or (j2+dj) < 0 or (j2+dj) >=c:
                          ans += float("-inf")
                      else:
                          ans += front[j1+di][j2+dj]
                      maxi = max(maxi, ans)
              cur[j1][j2] = maxi
      front = [row[:] for row in cur]
  return front[0][c-1]
              
