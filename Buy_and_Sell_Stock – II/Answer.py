### Answer 1
### Time complexity - O(N*2), Space compplexity - O(N*2)+O(N)
def getMaximumProfit(values, n) :

    dp = [[-1]*(2) for _ in range(n)]
    def buyandsellstock(i, buy):
        if i == n:
            return 0
        if dp[i][buy]!=-1:
            return dp[i][buy]
        profit = 0
        if buy:
            profit = max(-values[i] + buyandsellstock(i+1, False), 0+buyandsellstock(i+1,True))
        else:
            profit = max(values[i] + buyandsellstock(i+1, True), 0 + buyandsellstock(i+1, False))
        
        dp[i][buy] = profit
        return profit
    return buyandsellstock(0, True) if n >0 else 0
  
### Answer 2
### Time complexity - O(N*2), Space compplexity - O(N*2)
def getMaximumProfit(values, n) :

    dp = [[-1]*(2) for _ in range(n+1)]
    dp[n][0] = dp[n][1] = 0

    for i in range(n-1,-1,-1):
        for buy in range(2):
            profit = 0
            if buy==0:
                profit = max(-values[i] + dp[i+1][1], 0+dp[i+1][0])
            else:
                profit = max(values[i] + dp[i+1][0], 0 + dp[i+1][1])
        
            dp[i][buy] = profit
    return dp[0][0]

### Answer 2
### Time complexity - O(N*2), Space compplexity - O(1)
def getMaximumProfit(values, n) :

    ahead = [0,0]
    curr = ahead[:]

    for i in range(n-1,-1,-1):
        for buy in range(2):
            profit = 0
            if buy==0:
                profit = max(-values[i] + ahead[1], 0+ahead[0])
            else:
                profit = max(values[i] + ahead[0], 0 + ahead[1])
            curr[buy] =profit
        ahead = curr[:]

    return curr[0]
