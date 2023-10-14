"""
Given
S1 - S2 = D
S1>=S2

So,
S1 = TOTALSUM-S2

S2 = (TOTALSUM-D)/2
"""

### Answer 1 - Memoization approach
### Time complexity - O(N*K), Space complexity - O(N*K) +O(N)
def countPartitions(n: int, d: int, arr: List[int]) -> int:
    sump = sum(arr)
    ### if sump-d then its not possible
    if sump-d<0:
        return 0
    ### d not achieved from the sets
    if (sump-d)%2==1:
        return 0
    # only need to check the s2
    tar = (sump-d)//2
    dp = [[-1 for i in range(tar+1)] for j in range(n)]
    def find_subsets(index, target):
        if index == 0:
            """
            when index is 0 and array has 0 in the index and target is also zero we will consider 2
            [0,1]
            if target is 0 or target is equal to 0 index element then we will consider 1
            else 
            0
            """
            if target == 0 and arr[0]==0:
                return 2
            if target == 0 or target == arr[0]:
                return 1
            return 0
        
        if dp[index][target]!=-1:
            return dp[index][target]

        nonpick = find_subsets(index-1, target)
        pick = 0
        if (arr[index]<=target):
            pick = find_subsets(index-1, target-arr[index])
        dp[index][target] = (pick+nonpick)%int(1e9 + 7)
        return dp[index][target]
    return find_subsets(n-1, tar)
  
### Answer 2 - Tabulation approach - 2D array
### Time complexity - O(N*K), Space complexity - O(N*K)
def countPartitions(n: int, d: int, arr: List[int]) -> int:
    sump = sum(arr)
    if sump-d<0:
        return 0
    if (sump-d)%2==1:
        return 0
    tar = (sump-d)//2
    dp = [[-1 for i in range(tar+1)] for j in range(n)]
    def find_subsets(index, target):
        if index == 0:
            if target == 0 and arr[0]==0:
                return 2
            if target == 0 or target == arr[0]:
                return 1
            return 0
        
        if dp[index][target]!=-1:
            return dp[index][target]

        nonpick = find_subsets(index-1, target)
        pick = 0
        if (arr[index]<=target):
            pick = find_subsets(index-1, target-arr[index])
        dp[index][target] = (pick+nonpick)%int(1e9 + 7)
        return dp[index][target]
    return find_subsets(n-1, tar)

### Answer 3 - Tabulation approach - 1D array
### Time complexity - O(N*K), Space complexity - O(K)
def countPartitions(n: int, d: int, arr: List[int]) -> int:
    sump = sum(arr)
    if (sump - d) < 0 or (sump - d) % 2:
        return 0
    sump = (sump-d)//2

    dp = [[0]*(sump+1) for j in range(n)]
    if arr[0]==0:
        dp[0][0]=2
    else:
        dp[0][0]=1
    
    if arr[0]!=0 and arr[0]<=sump:
        dp[0][arr[0]]=1

    for index in range(1,n):
        for target in range(sump+1):
            nonpick = dp[index-1][target]
            pick = 0
            if (arr[index]<=target):
                pick = dp[index-1][target-arr[index]]
            dp[index][target] = (pick+nonpick)%int(1e9 + 7)
    return dp[n-1][sump]
