# Bottom-up approach of DP
# Time: O(n)
# Space: O(n)
def count_climb_stairs(n):
    stairs = [0] * (n + 1)
    if n == 0:
        return 0
    stairs[1] = 1
    stairs[2] = 2

    for i in range(3, n + 1):
        stairs[i] = stairs[i - 1] + stairs[i - 2]
    return stairs[n]


# Recursive approach
def count_climb_stairs_recur(i, n):
    if i > n:
        return 0
    if i == n:
        return 1

    return count_climb_stairs(i + 1, n) + count_climb_stairs(i + 2, n)


# Recursive with Memoization
def count_climb_stairs_memo(n, memo=None):
    if n in memo:
        return memo[n]

    if n <= 1:
        return 1
    memo[n] = count_climb_stairs_memo(n-1, memo=memo) + count_climb_stairs_memo(n - 2, memo=memo)
    return memo[n]


if __name__ == '__main__':
    print(count_climb_stairs(5))
    print(count_climb_stairs_memo(5, memo={}))