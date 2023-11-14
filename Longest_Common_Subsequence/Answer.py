### Answer 1 - DP, Memoization approach
### Time complexity - O(N*M),Space complexity - O(N*M) + O(N+M)
def lcs(s, t) :
	dp = [[-1 for i in range(len(t))] for j in range(len(s))]
	def findsolution(index1, index2):
		if index1 < 0 or index2 < 0:
			return 0
		if dp[index1][index2] != -1:
			return dp[index1][index2]
		if s[index1] == t[index2]:
			dp[index1][index2] = 1 + findsolution(index1 - 1, index2 - 1)
		else:
			dp[index1][index2] = 0 + max(findsolution(index1 - 1, index2), findsolution(index1, index2-1))
		return dp[index1][index2]
	return findsolution(len(s)-1,len(t)-1)

### Answer 2 - Tabulation approach
### Time complexity - O(N*M),Space complexity - O(N*M)
def lcs(s, t) :
	n = len(s)
	m = len(t)
	dp = [[-1 for i in range(m+1)] for j in range(n+1)]

	for i in range(n+1):
		dp[i][0] = 0
	
	for i in range(m+1):
		dp[0][i] = 0
	
	for i in range(1, n+1):
		for j in range(1, m+1):
			if s[i-1] == t[j-1]:
				dp[i][j] = 1+dp[i-1][j-1]
			else:
				dp[i][j] = max(dp[i-1][j],dp[i][j-1])
	
	return dp[n][m]

### Answer 3 - Tabulaiton with space optimization
### Time complexity - O(N*M),Space complexity - O(M)
def lcs(s, t) :
	n = len(s)
	m = len(t)
	prev = [0] * (m + 1)
	cur = [0] *	(m + 1)
	for i in range(1, n+1):
		for j in range(1, m+1):
			if s[i-1] == t[j-1]:
				cur[j] = 1+prev[j-1]
			else:
				cur[j] = max(prev[j],cur[j-1])
		prev = cur[:]
	return prev[m]

