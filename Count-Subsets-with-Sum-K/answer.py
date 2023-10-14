### Answer 1 - Memoization approach
### Time complexity - O(N*K)+O(N), Space complexity - O(N*K)
def findWays(arr: List[int], k: int) -> int:
    dp =[[-1]*(k+1) for j in range(len(arr))]

    def find_subs(index, target):
        if ind == 0:
            if target == 0 and arr[0] == 0:
                return 2
            if target == 0 or target == arr[0]:
                return 1
            return 0
            
        if dp[index][target]!=-1:
            return dp[index][target]

        nonpick = find_subs(index-1,target)
        pick = 0
        if arr[index]<=target:
            pick = find_subs(index-1, target-arr[index])
        dp[index][target] = pick + nonpick
        return dp[index][target]
    
    return find_subs(len(arr)-1, k)%1000000007

### Answer 2 - Tabulation approach - 2D array
### Time complexity - O(N*K), Space complexity - O(N*K)
def findWays(arr: List[int], k: int) -> int:
    n = len(arr)
    dp =[[0]*(k+1) for j in range(n)]

    for i in range(n):
        dp[i][0] = 1
    
    if arr[0]<=k:
        dp[0][arr[0]] = 1

    for index in range(1, n):
        for target in range(1, k+1):
            nonpick = dp[index-1][target]
            pick = 0
            if arr[index]<=target:
                pick = dp[index-1][target-arr[index]]
            dp[index][target] = pick + nonpick
            
    return dp[n-1][k]%1000000007

### Answer 3 - Tabulation approach - 1D array
### Time complexity - O(N*K), Space complexity - O(K)
def findWays(arr: List[int], k: int) -> int:
    n = len(arr)
    prev = [0 for i in range(k + 1)]

    prev[0] = 1
    
    if arr[0]<=k:
        prev[arr[0]] = 1

    for index in range(1, n):
        curr=[0 for i in range(k + 1)]
        curr[0]=1
        for target in range(1, k+1):
            nonpick = prev[target]
            pick = 0
            if arr[index]<=target:
                pick = prev[target-arr[index]]
            curr[target] = pick + nonpick
        prev = curr
            
    return prev[k]%10000007
