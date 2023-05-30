"""
Input: houses = [1,4,8,10,20], k = 3
Output: 5
Explanation: Allocate mailboxes in position 3, 9 and 20.
Minimum total distance from each houses to nearest mailboxes is |3-1| + |4-3| + |9-8| + |10-9| + |20-20| = 5
"""


def minDistance(A, k):
    A.sort()
    n = len(A)
    B = [0]
    for i, a in enumerate(A):
        B.append(B[i] + a)

    def cal(i, j):
        m1, m2 = (i + j) // 2, (i + j + 1) // 2
        return (B[j + 1] - B[m2]) - (B[m1 + 1] - B[i])

    dp = [cal(0, j) for j in range(n)]
    for k in range(2, k + 1):
        for j in range(n - 1, k - 2, -1):
            for i in range(k - 2, j):
                dp[j] = min(dp[j], dp[i] + cal(i + 1, j))
    return int(dp[-1])


print(minDistance([1, 4, 8, 10, 20], 3))

n=3
m=2

dp=[[0 for i in range(m)] for j in range(n)]
print(dp)