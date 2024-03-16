### Only positive values - using 2-pointer
### Time complexity - O(N), space Complexity - O(1)
def getLongestSubarray(a: [int], k: int) -> int:
    n = len(a) # size of the array.

    left, right = 0, 0 # 2 pointers
    Sum = a[0]
    maxLen = 0
    while right < n:
        # if sum > k, reduce the subarray from left
        # until sum becomes less or equal to k:
        while left <= right and Sum > k:
            Sum -= a[left]
            left += 1

        # if sum = k, update the maxLen i.e. answer:
        if Sum == k:
            maxLen = max(maxLen, right - left + 1)

        # Move forward the right pointer:
        right += 1
        if right < n: Sum += a[right]

    return maxLen

### for both positive and negative
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
