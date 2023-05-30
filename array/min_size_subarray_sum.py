from sys import maxsize


# Sliding window technique to find min length of sum
def min_size_subarray(nums, target):
    size = len(nums)
    min_length = maxsize

    low = 0
    high = 0  # window of size 1;
    sum = nums[0]
    while (low < size and high < size):
        # conditions
        if sum >= target:  # decrease the window size
            min_length = min(min_length, (high - low) + 1)
            sum -= nums[low]
            low += 1
        else:  # increase the window size
            high += 1
            if high < size:
                sum += nums[high]
    return min_length


if __name__ == '__main__':
    print(min_size_subarray([2, 3, 1, 2, 4, 3], 7))
