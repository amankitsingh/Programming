class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1]*(amount+1) for _ in range(n)]
        def coin(index, target):
            if index == 0:
                if target%coins[0] == 0:
                    return target//coins[0]
                else:
                    return int(1e9)
            if dp[index][target]!=-1:
                return dp[index][target]
            nonpick = coin(index-1, target)
            pick = int(1e9)
            if coins[index]<=target:
                pick = 1+coin(index,target-coins[index])
            dp[index][target] = min(nonpick, pick)
            return dp[index][target]
        ans = coin(n-1, amount)
        return -1 if ans == int(1e9) else ans