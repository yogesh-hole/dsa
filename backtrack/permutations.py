def generate_permutations(arr):
    result = []
    temp = []
    arr.sort()
    # generate(arr, result, temp, n)
    generate_unique_perms(arr, temp, result)
    return result


def generate_unique_perms(remainder, path, result):
    remainder = remainder[:]
    path = path[:]
    if len(remainder) == 0:
        result.append(path)

    for i in range(len(remainder)):
        if i > 0 and remainder[i] == remainder[i - 1]:
            continue
        path.append(remainder[i])
        generate_unique_perms(remainder[0:i] + remainder[i + 1:], path, result)
        path.pop()
    return


def generate(arr, result, temp, n):
    if len(temp) == n:
        result.append(temp[:])
        return
    for i in range(n):
        if arr[i] not in temp:
            temp.append(arr[i])
            generate(arr, result, temp, n)
            temp.pop()


# print(generate_permutations([1, 2, 3]))
print(generate_permutations([1, 1, 3]))
