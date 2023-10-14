### Answer 1 - memoization approach
### Time complexity - O(N*X), Space complexity - O(N*X) + O(S)
def minimumElements(num: List[int], x: int) -> int:
    dp = [[-1 for i in range(x+1)] for j in range(len(num))]
    def find_coin(index, target):
        if index==0:
            if target%num[0]==0:
                return target//num[index]
            return float("inf")
        if dp[index][target]!=-1:
            return dp[index][target]
        nottake = 0 + find_coin(index-1, target)
        take = float("inf")
        if num[index]<=target:
            take = 1 + find_coin(index,target-num[index])
        dp[index][target] = min(nottake, take)
        return dp[index][target]

    result = find_coin(len(num)-1, x)
    return -1 if result == float("inf") else result

### Answer 2 - Tabulation approach - 2D array
### Time complexity - O(N*X), Space complexity - O(N*X) 
def minimumElements(num: List[int], x: int) -> int:
    n = len(num)
    dp = [[-1 for i in range(x+1)] for j in range(n)]
    
    for i in range(x+1):
        if i%num[0]==0:
            dp[0][i] = i//num[0]
        else:
            dp[0][i] = float("inf")
    for index in range(1,n):
        for target in range(x+1):
            nottake = 0 + dp[index-1][target]
            take = float("inf")
            if num[index]<=target:
                take = 1 + dp[index][target-num[index]]
            dp[index][target] = min(nottake, take)

    return -1 if dp[n-1][x] == float("inf") else dp[n-1][x]

### Answer 3 - Tabulation approach - 1D array
### Time complexity - O(N*X), Space complexity - O(X) 
def minimumElements(num: List[int], x: int) -> int:
    n = len(num)
    prev = [0] * (x + 1)
    
    for i in range(x+1):
        if i%num[0]==0:
            prev[i] = i//num[0]
        else:
            prev[i] = float("inf")
    for index in range(1,n):
        curr = [0] * (x + 1)
        for target in range(x+1):
            nottake = 0 + prev[target]
            take = float("inf")
            if num[index]<=target:
                take = 1 + curr[target-num[index]]
            curr[target] = min(nottake, take)
        prev = curr

    return -1 if prev[x] == float("inf") else prev[x]
