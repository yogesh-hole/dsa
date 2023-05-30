from sys import maxsize
from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    coins.sort()
    dp = [maxsize] * (amount+1)
    dp[0]=0
    for i in range(1, amount+1):
        for coin in coins:
            if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
            else:
                break
    return dp[amount] if dp[amount] != maxsize else -1

#
# def coinChange(self, coins: List[int], amount: int) -> int:
#     n = len(coins)
#     coins.sort()
#     dp = [math.inf] * (amount+1)
#     dp[0] = 0
#
#     for amnt in range(1, amount+1):
#         for coin in coins:
#             if amnt >= coin:
#                 dp[amnt] = min(dp[amnt], dp[amnt-coin] + 1)
#             else:
#                 break  # optimize a bit
#
#     return dp[amount] if dp[amount] != math.inf else -1
#

print(coinChange([1, 2, 5], 11))
