### Answer 1 - top-down approach
### Time complexity - O(N*K), space complexity - O(N)+O(N*K) ~ O(N*K)
def subsetSumToK(n, k, arr):
    dp = [[-1 for i in range(k+1)] for j in range(n)]
    def find_target(index, target):
        if target == 0:
            return True
        
        if index == 0:
            return arr[index] == target

        if dp[index][target]!=-1:
            return dp[index][target]

        nonpick = find_target(index-1, target)
        pick = False
        if arr[index] <= target:
            pick = find_target(index-1, target - arr[index])
        dp[index][target] =  pick or nonpick
        return dp[index][target]
    return find_target(n-1, k)

### Answer 2 - bottom - up approach
### Time complexity - O(N*K), space complexity - O(N*K)
def subsetSumToK(n, k, arr):
    dp = [[False for i in range(k+1)] for j in range(n)]
    for i in range(n):
        dp[i][0] = True
    
    if arr[0] <= k:
        dp[0][arr[0]] = True
    
    for ind in range(1, n):
        for tar in range(1, k+1):
            nontake = dp[ind-1][tar]
            take = False
            if arr[ind] <= tar:
                take = dp[ind-1][tar - arr[ind]]
            dp[ind][tar] = nontake or take
    return dp[n-1][k]

### Answer 3 - bottom - up approach
### Time complexity - O(N*K), space complexity - O(K)
def subsetSumToK(n, k, arr):
    prev = [False]*(k+1)
    prev[0] = True

    if arr[0] <= k:
        prev[arr[0]] = True

    
    for ind in range(1, n):
        curr = [False]*(k+1)
        curr[0]=True
        for tar in range(1, k+1):
            nontake = prev[tar]
            take = False
            if arr[ind] <= tar:
                take = prev[tar - arr[ind]]
            curr[tar] = nontake or take
        prev = curr[:]
    return prev[k]



