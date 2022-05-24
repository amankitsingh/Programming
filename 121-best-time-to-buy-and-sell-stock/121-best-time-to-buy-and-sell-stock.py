class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        profit = 0
        for x in prices:
            if x < smallest:
                smallest = x
            elif x > smallest:
                profit = max(profit, x-smallest)
                    
            
        return profit