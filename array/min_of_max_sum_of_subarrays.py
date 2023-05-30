ans = 10000000


def solve(a, n, k, index, sum, maxsum):
    global ans

    # K=1 is the base Case
    if (k == 1):
        maxsum = max(maxsum, sum)
        sum = 0
        for i in range(index, n):
            sum += a[i]

        # we update maxsum
        maxsum = max(maxsum, sum)

        # the answer is stored in ans
        ans = min(ans, maxsum)
        return

    sum = 0

    # using for loop to divide the array into
    # K-subarray
    for i in range(index, n):
        sum += a[i]

        # for each subarray we calculate sum ans update
        # maxsum
        maxsum = max(maxsum, sum)

        # calling function again
        solve(a, n, k - 1, i + 1, sum, maxsum)


# driver code

arr = [1, 2, 3, 4]
k = 3  # K divisions
n = 4  # Size of Array
solve(arr, n, k, 0, 0, 0)
print(ans)
