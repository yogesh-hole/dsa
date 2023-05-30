graph = {
    'f': ['g', 'i'],
    'g': ['h', 'f'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}


def has_path(graph, source, dest):
    if source == dest:
        return True
    for i in graph[source]:
        if has_path(graph, i, dest):
            return True
    return False


def has_cycle(graph, source, dest, visited):
    if source == dest:
        return True
    if source in visited:
        return False
    visited.add(source)

    for i in graph[source]:
        if has_cycle(graph, i, dest, visited):
            return True
    return False


# print(has_path(graph, 'f', 'j'))
print(has_cycle(graph, 'f', 'g', set()))
