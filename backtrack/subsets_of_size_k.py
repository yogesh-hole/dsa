class Solution:

    def get_subsets(self, arr, index, temp, ans, k):
        if len(temp) == k:
            ans.append(list(temp))
            return

        for i in range(index, len(arr)):
            temp.append(arr[i])
            self.get_subsets(arr, i + 1, temp, ans, k)
            temp.pop()

    def subsets(self, arr, k):
        ans = []
        self.get_subsets(arr, 0, [], ans, k)
        return ans


sol = Solution()
print(sol.subsets([1, 2, 3, 4, 5], 3))
