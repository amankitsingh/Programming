### Answer 1 - Memoization approach
### Time complexity - O(P*N), Space complexity - O(P*N)+O(S)
def cutRod(price, n):
    dp = [[-1]*(n+1) for i in range(n)]
    def find_max_cuts(index, target):
        if target == 0:
            return 0
        if index==0:
            return price[index]*target
        if dp[index][target]!=-1:
            return dp[index][target]
        nottake = 0+find_max_cuts(index-1, target)
        take = float("-inf")
        if (index+1)<=target:
            take = price[index] + find_max_cuts(index, target-(index+1))
        dp[index][target] = max(nottake, take)
        return dp[index][target]
    return find_max_cuts(n-1,n)
  
### Answer 2 - Tabulation approach - 2D array
### Time complexity - O(P*N), Space complexity - O(P*N)
def cutRod(price, n):
    dp = [[0]*(n+1) for i in range(n+1)]
    for index in range(1, n+1):
        for target in range(1,n+1):
            nottake = 0 + dp[index-1][target]
            take = float("-inf")
            if (index)<=target:
                take = price[index-1] + dp[index][target-(index)]
            dp[index][target] = max(nottake, take)
    return dp[n-1][n]
  
### Answer 3 - Tabulation approach - 1D array
### Time complexity - O(P*N), Space complexity - O(P)
def cutRod(price, n):
    prev = [0]*(n+1)
    for index in range(1, n+1):
        curr = [0]*(n+1)
        for target in range(1,n+1):
            nottake = 0 + prev[target]
            take = float("-inf")
            if (index)<=target:
                take = price[index-1] + curr[target-(index)]
            curr[target] = max(nottake, take)
        prev = curr
    return prev[n]
