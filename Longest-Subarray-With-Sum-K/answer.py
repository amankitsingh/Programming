### Answer 1 - Brute force
def getLongestSubarray(nums: [int], k: int) -> int:
    n = len(nums)
    length = 0
    for i in range(n):
        s = 0
        for j in range(i,n):
            s += nums[j]
            if s == k:
                length = max(length, j-i+1)
    return length
### Answer 2 - usign hashmap
### Time complexity = O(N), Space complexity - O(N)
def getLongestSubarray(nums: [int], k: int) -> int:
    n = len(nums)
    result = {}
    prevSum= 0
    length=0
    for i in range(n):
        prevSum+=nums[i]
        if prevSum==k:
            length = max(length, i+1)
        rem = prevSum-k

        if rem in result:
            length = max(length, i - result[rem])
        if prevSum not in result:
            result[prevSum] = i
    return length
