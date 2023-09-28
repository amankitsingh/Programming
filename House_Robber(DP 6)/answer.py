### Answer 1 - DP - bottom up approach
### Time complexity - O(n), space complexity - O(1)
def robber(arr):
    prev2 = 0
    prev = arr[0]
    
    for i in range(1, len(arr)):
        pick = arr[i]
        if i > 1:
            pick+=prev2
        nonpick = 0 + prev
        curr = max(pick, nonpick)
        prev2 = prev
        prev = curr
    return prev

def takearray(houses):
    if len(houses) == 0:
      return 0
    if len(houses) == 1:
        return houses[0]
    arr1 = [houses[x] for x in range(1, len(houses))]
    arr2 = [houses[x] for x in range(0, len(houses)-1)]
    return max(robber(arr1), robber(arr2))

takearray([2,1,4,9])
