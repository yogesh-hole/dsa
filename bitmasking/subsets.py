def subset(A):
    n = len(A)
    res = list()
    for i in range(1 << n):     # each i represents a subset
        cur = list()
        for j in range(n):      # each j is a possible candidate for this subset
            if i & (1 << j):    # we should add j to the current subset
                cur.append(A[j])
        res.append(cur)
    return res

print(subset([1, 2, 3]))