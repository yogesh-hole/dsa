# 1. Dijkstra's Algorithm for finding shortest path
import heapq
from collections import defaultdict


def dijkstra_shortest_path(matrix, source, nodes):
    graph = defaultdict(list)
    for (u, v, w) in matrix:
        graph[u].append((v, w))

    priority_queue = [(0, source)]
    shortest_path = {}
    while len(priority_queue):
        current_weight, current_node = heapq.heappop(priority_queue)
        if not current_node in shortest_path:
            shortest_path[current_node] = current_weight
            for neighbor, weight in graph[current_node]:
                heapq.heappush(priority_queue, (current_weight + weight, neighbor))

    if len(shortest_path) == nodes:
        return max(shortest_path.values())
    return -1


# print(dijkstra_shortest_path([[2, 1, 1], [2, 3, 1], [3, 4, 1]], source=2, nodes=4))

# Bellman-Ford Algorithm for finding shortest path
def bellman_ford_shortest_path(matrix, source, nodes):
    distance = [float('inf')] * (nodes + 1)
    distance[source] = 0
    for i in range(nodes - 1):
        for (u, v, w) in matrix:
            distance[v] = min(distance[v], distance[u] + w)
    for (u, v, w) in matrix:
        if distance[v] > distance[u] + w:
            return -1
    return max(distance)


# Floyd Warshall Algorithm for finding shortest path
def floyd_warshall_shortest_path(matrix, nodes):
    distance = [[float('inf')] * (nodes + 1) for i in range(nodes + 1)]
    for i in range(nodes + 1):
        distance[i][i] = 0
    for (u, v, w) in matrix:
        distance[u][v] = w
    for k in range(nodes + 1):
        for i in range(nodes + 1):
            for j in range(nodes + 1):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    return max(max(distance))