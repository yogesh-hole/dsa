from itertools import accumulate


class Solution:
    def bestRotation(self, A):
        n = len(A)
        P = [1] * n
        for i in range(n):
            P[(i - A[i] + 1) % n] -= 1
        P = list(accumulate(P))
        return P.index(max(P))

s=Solution()
print(s.bestRotation([2, 3, 1, 4, 0]))