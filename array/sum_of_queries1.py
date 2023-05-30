class Solution:
    def querySum(self, n, arr, q, queries):
        i = 0
        result = []
        while q > 0:
            l, r = queries[i], queries[i + 1]
            sum = 0
            for k in range(l - 1, r):
                sum += arr[k]
            result.append(sum)
            q -= 1
            i += 2
        return result


s = Solution()
print(s.querySum(4, [1, 2, 3, 4], 2, [1, 4, 2, 3]))
