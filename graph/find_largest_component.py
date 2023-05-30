graph = {
    '0': ['8', '1', '5'],
    '1': ['0'],
    '5': ['0', '8'],
    '8': ['0', '5'],
    '2': ['3', '4'],
    '3': ['2', '4'],
    '4': ['3', '2']
}


def largestComponent(graph):
    result = 0
    for i in graph.keys():
        result = max(explore(graph, i, set()), result)
    return result


def explore(graph, node, visited):
    if node in visited:
        return 0
    visited.add(node)
    size = 1
    for i in graph[node]:
        size += explore(graph, i, visited)
        print(visited)
    return size


print(largestComponent(graph))
