from typing import List


class Solution:
    def alternating_sum(self,arr, n):
        even, odd = 0, 1
        sum = minus = 0
        if n==0:
            return 0

        while even < odd < n:
            sum += arr[even]
            minus += arr[odd]
            even += 2
            odd += 2
        return sum - minus


    def maxAlternatingSum(self, nums: List[int]) -> int:
        max_sum = 0
        for i in range(len(nums)):
            max_sum = max(self.alternating_sum(nums, i), max_sum)
        return max_sum



s = Solution()
print(s.maxAlternatingSum([4, 2, 5, 3]))
