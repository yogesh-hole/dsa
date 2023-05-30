from typing import List


def removeDuplicates(nums: List[int]) -> int:
    i = 1
    while i < len(nums):
        if nums[i] == nums[i-1]:
            nums.pop(i)
        else:
            i += 1
    return nums


print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
