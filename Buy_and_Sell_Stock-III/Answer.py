### Answer 1
### time complexity - O(N*2*3), Space complexity - O(N*2*3) + O(N)
def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    dp =[[[-1]*3 for _ in range(2)]for _ in range(n)]

    def buyandsellstock(day,buy,attempt):
        if day == n or attempt == 0:
            return 0
        
        if dp[day][buy][attempt]!=-1:
            return dp[day][buy][attempt]

        
        profit = 0

        if buy==1:
            profit = max(-prices[day]+buyandsellstock(day+1,0,attempt), 0 + buyandsellstock(day+1,1,attempt))
        else:
            profit = max(prices[day]+buyandsellstock(day+1,1,attempt-1), 0 + buyandsellstock(day+1,0,attempt))
        
        dp[day][buy][attempt] = profit
        return dp[day][buy][attempt]
    
    return buyandsellstock(0,1,2)

### Answer 2
### time complexity - O(N*2*3), Space complexity - O(N*2*3)
def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    dp =[[[0]*3 for _ in range(2)]for _ in range(n+1)]

    for day in range(n-1,-1,-1):
        for buy in range(2):
            for attempt in range(1,3):
                if buy==0:
                    profit = max(-prices[day]+dp[day+1][1][attempt],0 + dp[day+1][0][attempt])
                else:
                    profit = max(prices[day]+dp[day+1][0][attempt-1], 0 + dp[day+1][1][attempt])
        
                dp[day][buy][attempt] = profit
    return dp[0][0][2]

### Answer 3
### time complexity - O(N*2*3), Space complexity - O(2*3)~O(1)
def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    ahead = [[0 for _ in range(3)] for _ in range(2)]
    curr = ahead[:]

    for day in range(n-1,-1,-1):
        for buy in range(2):
            for attempt in range(1,3):
                if buy==0:
                    profit = max(-prices[day]+ahead[1][attempt],0 + ahead[0][attempt])
                else:
                    profit = max(prices[day]+ahead[0][attempt-1], 0 + ahead[1][attempt])
        
                curr[buy][attempt] = profit
        ahead = curr[:]
    return ahead[0][2]

### Answer 4
### time complexity - O(N*4), Space complexity - O(N*4)
### every even transaction we buy and odd we sell
def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    dp =[[-1]*4 for _ in range(n)]

    def buyandsellstock(day,transaction):
        if day == n or transaction == 4:
            return 0
        
        if dp[day][transaction]!=-1:
            return dp[day][transaction]

        profit = 0

        if transaction%2==0:
            profit = max(-prices[day]+buyandsellstock(day+1,transaction+1), 0 + buyandsellstock(day+1,transaction))
        else:
            profit = max(prices[day]+buyandsellstock(day+1,transaction+1), 0 + buyandsellstock(day+1,transaction))
        
        dp[day][transaction] = profit
        return dp[day][transaction]
    
    return buyandsellstock(0,0)
