def possible_coins(amount, coins):
    res=[]
    if amount == 0:
        return True
    if amount < 0:
        return False

    for c in coins:
        remainder = amount - c
        res.append(c)
        if possible_coins(remainder, coins):
            print(res)
            return True

    return False

print(possible_coins(4, [1,2,3]))