from typing import List


class Solution:
    def searchTarget(self, nums: List[int], target: int, low: int, high: int):
        if high > low:
            mid = (low + high) // 2
            if nums[low] == target:
                return low
            if nums[high] == target:
                return high
            elif nums[mid] <= target:
                return self.searchTarget(nums, target, low, mid)
            elif nums[mid] > target:
                return self.searchTarget(nums, target, mid, high)
        else:
            return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        if len(nums) == 1 and nums[0] != target:
            return [-1, -1]
        start = end = self.searchTarget(nums, target, 0, len(nums)-1)
        if start == -1 and end == -1:
            return [-1, -1]
        while end < len(nums):
            if len(nums) > 2 and nums[end] == nums[end + 1]:
                end += 1
            else:
                break
        return [start, end]


s = Solution()
print(s.searchRange([5, 7, 7, 8, 8, 10], 8))
print(s.searchRange([5, 7, 7, 8, 8, 10], 6))
print(s.searchRange([], 0))
print(s.searchRange([1], 0))
print(s.searchRange([1], 1))
print(s.searchRange([2, 2], 1))
print(s.searchRange([2, 2], 2))
