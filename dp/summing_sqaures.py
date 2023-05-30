import math


def summing_squares(n):
    return _summing_squares(n, {})


# Memoization
def _summing_squares(n, memo):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0

    min_squares = float('inf')
    for i in range(1, math.floor(math.sqrt(n) + 1)):
        square = i * i
        squares = 1 + _summing_squares(n - square, memo)
        min_squares = min(squares, min_squares)

    memo[n] = min_squares
    return min_squares


print(summing_squares(12))
print(summing_squares(8))
print(summing_squares(1))
print(summing_squares(2))
print(summing_squares(3))
print(summing_squares(6))
