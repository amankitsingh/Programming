### Answer 1
### Time complexity - O(N*2), Space complexity - O(N*2)+O(N)
def stockProfit(prices: List[int]) -> int:
    n = len(prices)
    dp = [[-1]*2 for _ in range(n)]

    def buyandsellstock(day, buy):
        if day >= n:
            return 0
        if dp[day][buy] != -1:
            return dp[day][buy]
        profit = 0
        if buy:
            profit = max(-prices[day] + buyandsellstock(day+1, False), 0 + buyandsellstock(day+1, True))
        else:
            profit = max(prices[day] + buyandsellstock(day+2, True), 0 + buyandsellstock(day+1, False))
        dp[day][buy] = profit
        return dp[day][buy]

    return buyandsellstock(0, True)

### Answer 2
### Time complexity - O(N*2), Space complexity - O(N*2)
def stockProfit(prices: List[int]) -> int:
    n = len(prices)
    dp = [[0]*2 for _ in range(n+2)]


    for day in range(n-1,-1,-1):
        for buy in range(2):
            profit = 0
            if buy==0:
                profit = max(-prices[day] + dp[day+1][1], 0 + dp[day+1][0])
            else:
                profit = max(prices[day] + dp[day+2][0], 0 + dp[day+1][1])
            dp[day][buy] = profit

    return dp[0][0]

### Answer 3
### Time complexity - O(N*2), Space complexity - O(2+2+2)~O(1)
def stockProfit(prices: List[int]) -> int:
    n = len(prices)
    ahead = [0,0]
    ahead1 = [0,0]
    curr = ahead[:]


    for day in range(n-1,-1,-1):
        for buy in range(2):
            profit = 0
            if buy==0:
                profit = max(-prices[day] + ahead[1], 0 + ahead[0])
            else:
                profit = max(prices[day] + ahead1[0], 0 + ahead[1])
            curr[buy] = profit
        ahead1 = ahead[:]
        ahead = curr[:]

    return curr[0]
