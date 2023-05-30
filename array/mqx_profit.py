from typing import List


def maxProfit(prices: List[int]) -> int:
    profit = 0
    i = 0
    while i < len(prices):
        j = i + 1
        max = 0
        while j < (len(prices)):
            if prices[j] > prices[i]:
                max = prices[j]
            j += 1
        if max:
            profit += max - prices[i]
            i = j
        i += 1
    return profit


def maxProfit1(prices: List[int]) -> int:
    profit = 0
    for idx in range(len(prices) - 1):

        if prices[idx] < prices[idx + 1]:
            profit += prices[idx + 1] - prices[idx]

    return profit


print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit1([7, 1, 5, 3, 6, 4]))
print(maxProfit1([1, 2, 3, 4, 5]))
