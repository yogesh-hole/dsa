graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}


def dfs_print(graph, source):
    stack = []
    stack.append(source)
    while len(stack):
        current = stack.pop()
        print(current)
        for i in graph[current]:
            stack.append(i)
    return


def dfs_recursive(graph, source, output):
    output.append(source)
    for i in graph[source]:
        dfs_recursive(graph, i, output)
    return output


# dfs_print(graph, 'a')
print(dfs_recursive(graph, 'a', []))
