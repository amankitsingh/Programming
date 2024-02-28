class Solution:
    def coinChange(self, arr: List[int], T: int) -> int:
        n = len(arr)
        prev = [0] * (T + 1)
        cur = [0] * (T + 1)
        
        for i in range(0, 1 + T):
            if i % arr[0] == 0:
                prev[i] = i // arr[0]
            else:
                prev[i] = int(1e9)
        for ind in range(1, n):
            for target in range(T + 1):
                not_take = prev[target]
                take = int(1e9)
                if arr[ind] <= target:
                    take = 1 + cur[target - arr[ind]]
                cur[target] = min(not_take, take)
            prev = cur 
        ans = prev[T]
        if ans >= int(1e9):
            return -1
        return ans