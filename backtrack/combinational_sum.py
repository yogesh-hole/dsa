'''
Given an array of positive integers arr[] and an integer x,
The task is to find all unique combinations in arr[] where the sum is equal to x.
The same repeated number may be chosen from arr[] an unlimited number of times.
Elements in a combination (a1, a2, …, ak) must be printed in non-descending order. (ie, a1 <= a2 <= … <= ak).
If there is no combination possible print “Empty”.
Input: arr[] = 2, 4, 6, 8, x = 8
Output:
[2, 2, 2, 2]
[2, 2, 4]
[2, 6]
[4, 4]
[8]
'''


def combinationSum(arr, sum):
    result = []
    temp = []

    # first do hashing nothing but set{}
    # since set does not always sort
    # removing the duplicates using Set and
    # Sorting the List
    arr = sorted(list(set(arr)))
    find_numbers(arr, 0, sum, result, temp)
    return result


def find_numbers(arr, index, sum, result, temp):
    if sum == 0:
        result.append(list(temp))
        return

    for i in range(index, len(arr)):
        # checking that sum does not become negative
        if sum - arr[i] >= 0:
            temp.append(arr[i])
            find_numbers(arr, i, sum - arr[i], result, temp)

            # removing element from list ( backtrack)
            temp.remove(arr[i])


# Driver Code
arr = [2, 4, 6, 8]
sum = 8
ans = combinationSum(arr, sum)

# If result is empty, then
if len(ans) <= 0:
    print("empty")

# print all combinations stored in ans
for i in range(len(ans)):

    print("(", end=' ')
    for j in range(len(ans[i])):
        print(str(ans[i][j]) + " ", end=' ')
    print(")", end=' ')
