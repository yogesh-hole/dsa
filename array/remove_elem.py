from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        for j in range(n):
            if nums[j] != val:
                # remove current element at 0 append -1 at last
                # adjust the remaining array elements
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1

        return i


s = Solution()
count = s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
print(count)
