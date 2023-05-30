graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}


def bfsTraverse(graph, source):
    queue = []
    result = []
    queue.append(source)
    while len(queue):
        current = queue.pop(0)
        result.append(current)
        for i in graph[current]:
            queue.append(i)

    return result


print(bfsTraverse(graph, 'a'))
