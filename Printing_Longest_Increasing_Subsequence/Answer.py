### Answer 1
### Time complexity - O(N*2), Space complexity - O(2N)~O(N)
def printingLongestIncreasingSubsequence(arr: List[int], n: int) -> List[int]:
  dp = [1]*n
  lastIndex = 0
  temp_hash = [i for i in range(n)]
  maxi = 0
  for i in range(1,n):
    for prev in range(i-1,-1,-1):
      if dp[prev]<dp[i] and 1+dp[prev]>dp[i]:
        dp[i] = 1+dp[prev]
        temp_hash[i] = prev
    if dp[i] > maxi:
      maxi = dp[i]
      lastIndex = i

  result = arr[lastIndex]
  while temp_hash[lastIndex] != lastIndex:
    lastIndex = temp_hash[lastIndex]
    result.append(arr[lastIndex])

  result.reverse()
  return result
