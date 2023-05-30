# Brute force solution with recursion
def count_unique_bst(n):
    if n == 1 or n == 0:
        return 0
    count_left = count_right = count = 0
    for i in range(n):
        count_left = count_unique_bst(i)
        count_right = count_unique_bst(n - 1 - i)
        count += count_left * count_right

    return count


# Top Down approach with Memoization - Dynamic Programming
def get_bst_count(n):
    count = [-1] * n + 1
    count_unique_bst_top_down(n, count=[])


def count_unique_bst_top_down(i, count=None):
    # base case
    if i == 0 or i == 1:
        return 1

    # Check if already computed
    if count[i] != -1:
        return count[i]

    result = 0
    for j in range(i + 1):
        result += count_unique_bst_top_down(j - 1, count=count) * count_unique_bst_top_down(i - j, count=count)

    # memoize the result
    count[i] = result
    return result


# Bottom up approach with Dynamic programming
def count_unique_bst_bottom_up(n):
    count = [0] * (n + 1)
    count[0] = 1
    count[1] = 1
    for i in range(2, n+1):
        count[i] = 0
        for j in range(i):
            count[i] += count[j] * count[i - j - 1]
    return count[n]


print(count_unique_bst_bottom_up(3))
