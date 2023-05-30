# def find_max_jumps(nums):
#     m = 0
#     for i, n in enumerate(nums):
#         if i > m: return False
#         m = max(m, i + n)
#     return True

# Recursive
def can_jump(arr, index):
    if index >= len(arr) - 1:
        return True

    max_jump = arr[index]
    while max_jump > 0:
        if can_jump(arr, index + 1):
            return True
        max_jump -= 1
    return False


# Recursive with Memoization
def can_jump_memo(arr, index, dp):
    if index >= len(arr) - 1:
        return True
    if dp[index] != -1:
        return dp[index]

    max_jump = arr[index]
    while max_jump > 0:
        if can_jump(arr, index + 1):
            dp[index] = True
            return True
        max_jump -= 1
    dp[index]=False
    return False


def find_max_jumps_tabulation(nums):
    n = len(nums)
    dp = [-1] * (len(nums))
    dp[n - 1] = 1
    for i in range(n - 2, -1, -1):
        j = i + 1
        maxjumps = nums[i]
        while maxjumps:
            if j > n - 1:
                dp[i] = 1
            else:
                dp[i] = dp[j]
            if dp[i] == 1:
                break
            maxjumps -= 1
        if dp[i] == -1:
            dp[i] = 0
    return dp[0]


def find_max_jumps(nums):
    dp = [-1] * (len(nums))
    return can_jump_memo(nums, 0, dp)


print(can_jump([2, 3, 1, 1, 4], 0))
print(find_max_jumps([2, 3, 1, 1, 4]))


# grid traveller using dp
def grid_traveller(m, n, dp):
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    if dp[m][n] != -1:
        return dp[m][n]
    dp[m][n] = grid_traveller(m - 1, n, dp) + grid_traveller(m, n - 1, dp)
    return dp[m][n]

def grid_traveller_using_bottom_up(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[1][1] = 1
    for i in range(m + 1):
        for j in range(n + 1):
            if i + 1 <= m:
                dp[i + 1][j] += dp[i][j]
            if j + 1 <= n:
                dp[i][j + 1] += dp[i][j]
    return dp[m][n]

# grid traveller with obstacles using dp
def grid_traveller_with_obstacles(m, n, dp, grid):
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    if dp[m][n] != -1:
        return dp[m][n]
    if grid[m - 1][n - 1] == 1:
        return 0
    dp[m][n] = grid_traveller_with_obstacles(m - 1, n, dp, grid) + grid_traveller_with_obstacles(m, n - 1, dp, grid)
    return dp[m][n]