### Answer 1 - Memoization approach
### Time complexity - O(N*totsum)+O(N)+O(N), Space complexity - O(N*K) +O(N)
def minSubsetSumDifference(arr: List[str], n: int) -> int:
    totsum = sum(arr)
    dp =[[-1 for i in range(totsum+1)] for j in range(n)]
    def subsetsService(index, target, dp):
        if target == 0:
            return True
        
        if index == 0:
            return arr[0] == target
        
        if dp[index][target]!=-1:
            return dp[index][target]
        
        nonpick = subsetsService(index-1, target,dp)
        pick = False
        if arr[index] <= target:
            pick = subsetsService(index-1,target-arr[index],dp)
        
        dp[index][target] = nonpick or pick
        return dp[index][target]
        
    for i in range(totsum+1):
        subsetsService(n-1, i, dp)
    
    mini = float("inf")
    
    for i in range(totsum+1):
        if dp[n-1][i] == True:
            mini = min(mini, abs(i - (totsum-i)))
    return mini

### Answer 2 - Tabulation approach - 2D array
### Time complexity - O(N*totsum)+O(N)+O(N), Space complexity - O(N*K)
def minSubsetSumDifference(arr: List[str], n: int) -> int:
    totsum = sum(arr)
    dp =[[False for i in range(totsum+1)] for j in range(n)]
    for i in range(n):
        dp[i][0] = True
    
    if arr[0]<=totsum:
        dp[0][arr[0]] = True
        
    for index in range(1,n):
        for target in range(1,totsum+1):
            nonpick = dp[index-1][target]
            pick = False
            if arr[index] <= target:
                pick = dp[index-1][target-arr[index]]            
            dp[index][target] = nonpick or pick
        
    mini = float("inf")
    
    for i in range(totsum+1):
        if dp[n-1][i] == True:
            mini = min(mini, abs(i - (totsum-i)))
    return mini
    
### Answer 3 - Tabulation approach - 1D array
### Time complexity - O(N*totsum)+O(N)+O(N), Space complexity - O(totsum)
def minSubsetSumDifference(arr: List[str], n: int) -> int:
    totsum = sum(arr)
    prev = [False]*(totsum+1)
    prev[0] = True
    if arr[0]<=totsum:
        prev[arr[0]] = True
        
    for index in range(1,n):
        curr = [False]*(totsum+1)
        for target in range(1,totsum+1):
            nonpick = prev[target]
            pick = False
            if arr[index] <= target:
                pick = prev[target-arr[index]]            
            curr[target] = nonpick or pick
        prev = curr
        
    mini = float("inf")
    
    for i in range(totsum+1):
        if prev[i] == True:
            mini = min(mini, abs(i - (totsum-i)))
    return mini
    
