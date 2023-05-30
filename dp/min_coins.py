# User function Template for python3
class Solution:

    def countCoins(self, V, coins, index):
        if V == 0:
            return 0
        if V < 0:
            return float('inf')
        if index <= 0 and V >= 1:
            return float('inf')
        return min(self.countCoins(V, coins, index - 1), 1 + self.countCoins(V - coins[index - 1], coins, index))
        #
        # if coins[index] <= V:
        #     count=self.countCoins(V - coins[index], count + 1, coins, index - 1)
        #     count -= 1

    def minCoins(self, coins, M, V):
        # code here
        return self.countCoins(V, coins, M - 1)


# find minumm number of coins
def get_minimum_coins_recursive(coins, m, v):
    if v == 0:
        return 0
    if v < 0:
        return float('inf')
    if m <= 0 and v >= 1:
        return float('inf')

    return min(get_minimum_coins_recursive(coins, m - 1, v),
               1 + get_minimum_coins_recursive(coins, m, v - coins[m - 1]))


if __name__ == '__main__':
    V = 30
    M = 2
    coins = [25, 10, 5]
    sol = Solution()
    count = sol.minCoins(coins, M, V)
    print(count)
    count = get_minimum_coins_recursive(coins, M, V)
    print(count)
