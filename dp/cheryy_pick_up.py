def cherryPickup(grid):
    N = len(grid)
    M = (N << 1) - 1
    dp = [[0] * N for _ in range(N)]
    dp[0][0] = grid[0][0]

    for n in range(1, M):
        for i in range(N - 1, -1, -1):
            for p in range(N - 1, -1, -1):
                j = n - i
                q = n - p

        if (j < 0 or j >= N or q < 0 or q >= N or grid[i][j] < 0 or grid[p][q] < 0):
            dp[i][p] = -1
            continue

        if (i > 0):
            dp[i][p] = max(dp[i][p], dp[i - 1][p])
        if (p > 0):
            dp[i][p] = max(dp[i][p], dp[i][p - 1])
        if (i > 0 and p > 0):
            dp[i][p] = max(dp[i][p], dp[i - 1][p - 1])

        if (dp[i][p] >= 0):
            dp[i][p] += grid[i][j] + (grid[p][q] if i != p else 0)

    return max(dp[N - 1][N - 1], 0)


grid = [[0, 1, -1], [1, 0, -1], [1, 1, 1]]
print(cherryPickup(grid))
