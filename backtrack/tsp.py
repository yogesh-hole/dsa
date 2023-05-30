result = []


def tsp(graph, visited, count, n, current_pos, cost):
    if count == n and graph[current_pos][0]:
        result.append(cost + graph[current_pos][0])
        return

    for i in range(n):
        if visited[i] is False and graph[current_pos][i]:
            visited[i] = True
            tsp(graph, visited, count + 1, n, i, cost + graph[current_pos][i])
            visited[i] = False


# Driver code

# n is the number of nodes i.e. V
if __name__ == '__main__':
    n = 4
    graph = [[0, 10, 15, 20],
             [10, 0, 35, 25],
             [15, 35, 0, 30],
             [20, 25, 30, 0]]

    # Boolean array to check if a node
    # has been visited or not
    v = [False for i in range(n)]

    # Mark 0th node as visited
    v[0] = True

    # Find the minimum weight Hamiltonian Cycle
    tsp(graph, v, 1, n, 0, 0)

    # ans is the minimum weight Hamiltonian Cycle
    print(min(result))
