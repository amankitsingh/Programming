### Answer 1
### Time complexity - O(N*N+N*N + N), Space complexity - O(N) 
def longestBitonicSubsequence(arr: List[int], n: int) -> int:
    dp1 = [1]*n
    dp2 = dp1[:]
    maxi = 0
    for i in range(n):
        for prev in range(i):
            if arr[i] > arr[prev]:
                dp1[i] = max(dp1[i], 1+dp1[prev])
    
    for i in range(n-1,-1,-1):
        for prev in range(n-1,i,-1):
            if arr[i] > arr[prev]:
                dp2[i] = max(dp2[i], 1+dp2[prev])
    
    maxi = 0
    for i in range(n):
        maxi = max(maxi, dp1[i]+dp2[i]-1)
    return maxi
                
