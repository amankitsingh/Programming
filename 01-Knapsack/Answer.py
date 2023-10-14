### Answer 1 - Memoization approach
### Time complexity - O(N*W),Space complexity - O(N*W)+O(stack)
def knapsack(W,weights, values, n):
    dp = [[-1 for i in range(W+1)] for j in range(n)]
    def find_max_rob(index, w):
        if index == 0:
            if weights[0]<=w:
                return values[0]
            return 0

        if dp[index][w]!=-1:
            return dp[index][w]
        
        nonpick = 0 +find_max_rob(index-1, w)
        pick = float("-inf")
        if weights[index]<=w:
            pick = values[index] + find_max_rob(index-1, w-weights[index])
        dp[index][w] = max(pick,nonpick)
        return dp[index][w]

    return find_max_rob(n-1, W)

### Answer 2 - Tabulation approach - 2D array
### Time complexity - O(N*W),Space complexity - O(N*W)
def knapsack(W,weights, values, n):
    dp = [[0 for i in range(W+1)] for j in range(n)]

    for i in range(weights[0], W+1):
        dp[0][i] = values[0]
    
    for index in range(1, n):
        for w in range(W+1):        
            nonpick = 0 + dp[index-1][w]
            pick = float("-inf")
            if weights[index]<=w:
                pick = values[index] + dp[index-1][w-weights[index]]
            dp[index][w] = max(pick,nonpick)
    return dp[n-1][W]
  
### Answer 3 - Tabulation approach - 1D array
### Time complexity - O(N*W),Space complexity - O(W)
def knapsack(W,weights, values, n):
    prev = [0]*(W+1)

    for i in range(weights[0], W+1):
        prev[i] = values[0]
    
    for index in range(1, n):
        for w in range(W,-1,-1):        
            nonpick = 0 + prev[w]
            pick = float("-inf")
            if weights[index]<=w:
                pick = values[index] + prev[w-weights[index]]
            prev[w] = max(pick,nonpick)
    return prev[W]
