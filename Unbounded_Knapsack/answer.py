### Answer 1 - top - down approach
### Time complexity - O(n*w), Space complexity - O(n*w) + O(N)
def unboundedKnapsack(n: int, w: int, val: List[int], wt: List[int]) -> int:
    dp = [[-1 for i in range(w+1)] for j in range(n)]
    def findmaxsteal(ind, W):
        
        if ind == 0:
            return (W//wt[0])*val[0]
        if dp[ind][W]!=-1:
            return dp[ind][W]
        nottake = 0 + findmaxsteal(ind-1,W)
        take = float("-inf")
        if wt[ind]<=W:
            take = val[ind] + findmaxsteal(ind,W-wt[ind])
        
        dp[ind][W] =  max(take,nottake)
        return dp[ind][W]

    
    return findmaxsteal(len(wt)-1, w)

### Answer 2 - top - down approach
### Time complexity - O(n*w), Space complexity - O(n*w)
def unboundedKnapsack(n: int, w: int, val: List[int], wt: List[int]) -> int:
    dp = [[0 for i in range(w+1)] for j in range(n)]

    for i in range(wt[0], w + 1, wt[0]):
        dp[0][i] = ((i // wt[0]) * val[0])

    for i in range(1,n):
        for j in range(w+1):        
            nottake = 0 + dp[i-1][j]
            take = float("-inf")
            if wt[i]<=j:
                take = val[i] + dp[i][j-wt[i]]
            dp[i][j] = max(take,nottake)
    return dp[n-1][w]

### Answer 3 - top - down approach
### Time complexity - O(n*w), Space complexity - O(w+1)
def unboundedKnapsack(n: int, w: int, val: List[int], wt: List[int]) -> int:
    prev = [0]*(w+1)

    for i in range(wt[0], w + 1, wt[0]):
        prev[i] = ((i // wt[0]) * val[0])

    for i in range(1,n):
        temp = [0]*(w+1)
        for j in range(w+1):        
            nottake = 0 + prev[j]
            take = float("-inf")
            if wt[i]<=j:
                take = val[i] + temp[j-wt[i]]
            temp[j] = max(take,nottake)
        prev = temp
    return prev[w]

### Answer 3 - top - down approach
### Time complexity - O(n*w), Space complexity - O(w+1)
def unboundedKnapsack(n: int, w: int, profit: List[int], weight: List[int]) -> int:
    dp = [0]*(w+1)

    for i in range(0, w + 1):
        for j in range(0, n):
            if weight[j] <= i:
                dp[i] = max(dp[i], profit[j] + dp[i - weight[j]])
    return dp[w]
