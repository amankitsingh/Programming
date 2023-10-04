### Answer 1 - top down approach
### Time complexity - O(M*N), space complexity - O(N)
def uniquePaths(m, n):
	prev = [0]*n
	for i in range(m):
		temp = [0]*n
		for j in range(n):
			if i == 0 and j == 0:
				temp[j] = 1
				continue
			up = 0
			left = 0
			if i > 0:
				up = prev[j]
			if j > 0:
				left = temp[j-1]
			temp[j] = up+left
		prev = temp
	return prev[n-1]
  
### Answer 2 - bottom - up approach
### Time complexity - O(M*N), space complexity - O(M-1)+O(N-1)
def uniquePaths(m, n):
	unq_path = 0
	def dfs(x,y):
		if m-1 == x and n-1 == y:
			nonlocal unq_path
			unq_path+=1
			return
		if x < m and y < n:
			path_follow = [(1,0),(0,1)]
			for i,j in path_follow:
				new_x = x + i
				new_y = y + j
				dfs(new_x,new_y)
		return
	dfs(0,0)
	return unq_path

### Answer 3 - matrix solution
### Time complexity - O(M-1*N-1), space complexity - O(M*N)
def uniquePaths(m, n):
	unq_path = 0
	dp = [[-1 for j in range(n)] for i in range(m)]
	dp[m-1][n-1] = 1
	for i in range(n):
		dp[m-1][i] = 1

	for i in range(m):
		dp[i][n-1] = 1
	
	for i in range(m-2,-1,-1):
		for j in range(n-2,-1,-1):
			dp[i][j] = dp[i+1][j]+dp[i][j+1]
	return dp[0][0]

### Answer 4 - maths solution
### Time complexity - O(1), space complexity - O(1)
def uniquePaths(m, n):
	return factorial(m+n-2)//(factorial(n-1)*factorial(m-1))
