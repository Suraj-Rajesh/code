#
# https://leetcode.com/problems/coin-change/
#

coins = [1,2,5]
amount = 11

def min_coins(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    coins.sort()

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin]) + 1
            else:
                break
    return dp[amount] if dp[amount] < amount + 1 else -1

print(min_coins(coins, amount))
