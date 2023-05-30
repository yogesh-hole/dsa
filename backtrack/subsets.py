class Solution:

    def backtrack(self, arr, i, temp, ans):
        if i == len(arr):
            ans.append(list(temp))
            return

        temp.append(arr[i])
        self.backtrack(arr, i + 1, temp, ans)
        temp.pop()
        self.backtrack(arr, i + 1, temp, ans)

    def subsets(self, arr):
        ans = []
        temp = []
        self.backtrack(arr, 0, temp, ans)
        return ans


sol = Solution()
print(sol.subsets([1, 2, 3]))
