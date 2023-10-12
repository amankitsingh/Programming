### Answer 1 - memoization approach
### Time complexity - O(N*K), Space complexity - O(N*K)*O(N)
def canPartition(arr, n):
    tsump = sum(arr)
    if tsump%2==1:
        return False
    dp = [[-1 for i in range(tsump+1)]for j in range(n)]
    def find_sum(index, sump):
        if sump == 0:
            return True
        if index == 0:
            return arr[index] == sump
        if dp[index][sump] != -1:
            return dp[index][sump]
        nonpick = find_sum(index-1, sump)
        pick = False
        if(arr[index]<=sump):
            pick = find_sum(index-1, sump-arr[index])
        dp[index][sump] = pick or nonpick
        return dp[index][sump]
    return find_sum(n-1, tsump//2)

### Answer 2 - tabulation approach - 2D array
### Time complexity - O(N*K), Space complexity - O(N*K)
def canPartition(arr, n):
  tsump = sum(arr)
  if tsump%2==1:
      return False
  dp = [[False for i in range(tsump+1)]for j in range(n)]
  for i in range(n):
      dp[i][0] = True
  k = tsump//2
  if arr[0] <= k:
      dp[0][arr[0]] = True
  for index in range(1,n):
      for sump in range(1,k+1):
          nonpick = dp[index-1][sump]
          pick = False
          if(arr[index]<=sump):
              pick = dp[index-1][sump-arr[index]]
          dp[index][sump] = pick or nonpick
  return dp[n-1][k]
### Answer 3 - tabulation approach - 1D array
### Time complexity - O(N*K), Space complexity - O(K)
def canPartition(arr, n):
    tsump = sum(arr)
    if tsump%2==1:
        return False
    k = tsump//2
    prev = [False]*(k+1)
    prev[0] = True
    if arr[0] <= k:
        prev[arr[0]] = True
    for index in range(1,n):
        temp = [False]*(k+1)
        temp[0] = True
        for sump in range(1,k+1):
            nonpick = prev[sump]
            pick = False
            if(arr[index]<=sump):
                pick = prev[sump-arr[index]]
            temp[sump] = pick or nonpick
        prev = temp
    return prev[k]
