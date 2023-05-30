
def count_bit(n):
    res = 0
    while n:
        if n & 1:
            res += 1
        n >>= 1
    return res


def count_bit1(n):
    res = 0
    while n:
        n = n & (n - 1)
        res += 1
    return res


def pow(x, n):
    res = 1
    while n:
        if n & 1:
            res *= x
        n >>= 1
        x *= x
    return res

print(count_bit(3))
print(count_bit1(3))
print(pow(2,3))