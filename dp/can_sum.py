# Top Down approach using Memoization
def sum_possible(amount, numbers, memo):
    if amount == 0:
        return True
    if amount < 0:
        return False
    for i in numbers:
        if sum_possible(amount - i, numbers, memo):
            memo[amount] = True
            return True

    memo[amount] = False
    return False


# print(sum_possible(13, [6, 2, 1], {}))

def sum_possible_tabular(amount, numbers):
    table = [False] * (amount + 1)
    table[0] = True
    for i in range(amount):
        if table[i]:
            for num in numbers:
                if num <= amount and (i + num) <= amount:
                    table[i + num] = True
    return table[amount]


print(sum_possible_tabular(13, [6, 8, 3]))
