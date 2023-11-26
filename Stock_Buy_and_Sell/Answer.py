### Answer
### Time complexity - O(N), Space complexity - O(1)
### intuition
"""
first check for the lowest and keep track fo the max profit and find the mini in the seen range.
"""

def maximumProfit(prices):
    maxprofit = 0
    mini = prices[0]

    for i in range(1,len(prices)):
        currprofit = prices[i] - mini
        maxprofit = max(maxprofit, currprofit)
        mini = min(mini, prices[i])
    
    return maxprofit
