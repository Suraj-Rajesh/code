#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#

# NOTE: only one transaction allowed, not multiple

prices = [7, 1, 5, 3, 6, 4]

def max_profits(prices):
    profit = 0
    minval = float('inf')
    for price in prices:
        if price < minval:
            minval = price
        else:
            profit = max(profit, price - minval)
    return profit


print(max_profits(prices))

#
# alternate
# 
def max_profits(prices):
    profit = 0
    minval = prices[0]
    for i in range(1, len(prices)):
        profit = max(profit, prices[i] - minval)
        minval = min(minval, prices[i])
    return profit
