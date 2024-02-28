class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1]*(amount+1) for _ in range(n)]
        def coin(index, target):
            if index == 0:
                return 1 if target%coins[0]==0 else 0
            
            if dp[index][target]!=-1:
                return dp[index][target]
            nonpick = coin(index-1,target)
            pick = 0
            if coins[index]<=target:
                pick = coin(index, target-coins[index])
            
            dp[index][target] = nonpick+pick
            return dp[index][target]
        return coin(n-1, amount)