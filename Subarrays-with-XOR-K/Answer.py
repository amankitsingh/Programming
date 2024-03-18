### Similar to count the subarray with target x (positive and negative)
### Time complexity - O(N), Space complexity - O(N)
from collections import defaultdict
def subarraysWithSumK(a: [int], b: int) -> int:
    result = defaultdict(int)
    result[0] = 1
    xr = 0
    cnt = 0
    n = len(a)
    for i in range(n):
        xr= xr ^ a[i] 
        x = xr^b
        cnt+=result[x]
        result[xr]+=1
    return cnt
