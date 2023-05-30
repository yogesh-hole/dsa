arr = [1, 2, 3]
# [],
# [1],
# [1,2]
# [1,3]
# [1,4]
# [1,2,3]


subset = []
index = 0


def subsets_utils(arr, index, subsets):
    print(*subsets)

    for i in range(index, len(arr)):
        subsets.append(arr[i])
        subsets_utils(arr, i + 1, subsets)
        subsets.pop(-1)


def get_subsets(arr):
    subsets = []
    index = 0
    res = subsets_utils(arr, index, subsets)
    print(res)

get_subsets(arr)