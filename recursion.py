# integer break
def integer_break(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 1

    max_product = n
    for i in range(1, n):
        max_product = max(max_product, i * integer_break(n - i))
    return max_product

def integer_break_dp(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        for j in range(1, i):
            dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
    return dp[n]
print(integer_break_dp(10))
print(integer_break_dp(2))
print(integer_break_dp(1))
