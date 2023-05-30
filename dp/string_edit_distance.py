# Bottom up approach using 2D array
def edit_distance(x: str, y: str, m: int, n: int):
    dp = [[0] * n] * m
    for i in range(m):
        dp[i][0] = i

    for j in range(n):
        dp[0][j] = j

    for i in range(1, m):
        for j in range(1, n):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
    return dp[m-1][n-1]


print(edit_distance("horse", "ros", 5, 3))
print(edit_distance("sunday", "saturday", 6, 8))
