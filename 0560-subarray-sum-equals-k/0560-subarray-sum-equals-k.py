class Solution:
    def subarraySum(self, arr: List[int], k: int) -> int:
        n = len(arr) # size of the given array.
        mpp = defaultdict(int)
        preSum = 0
        cnt = 0

        mpp[0] = 1 # Setting 0 in the map.
        for i in range(n):
            # add current element to prefix Sum:
            preSum += arr[i]

            # Calculate x-k:
            remove = preSum - k

            # Add the number of subarrays to be removed:
            cnt += mpp[remove]

            # Update the count of prefix sum
            # in the map.
            mpp[preSum] += 1

        return cnt
