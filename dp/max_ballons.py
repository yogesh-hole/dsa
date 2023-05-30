from typing import List

def maxCoins(nums: List[int]) -> int:
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    # iterate the input array in reverse order to fill the dp table
    for i in range(n - 2, -1, -1):
        for j in range(i + 2, n):
            for k in range(i + 1, j):
                dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])

    return dp[0][n - 1]


print(maxCoins([3, 1, 5, 8]))
