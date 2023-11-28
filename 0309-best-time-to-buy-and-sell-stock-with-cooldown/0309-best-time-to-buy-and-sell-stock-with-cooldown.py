class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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
        