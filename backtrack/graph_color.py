V = 4


# A function to print the color configuration

def printSolution(color):
    print("Solution Exists: Following are the assigned colors ")
    for c in color:
        print(c, end=" ")
    print()


# A utility function to check if the current color assignment is safe for vertex v
def isSafe(v, graph, color, c):
    for i in range(V):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True


def graphColoringUtil(graph, m, color, current_vertex):
    if current_vertex == V:
        return True

    for c in range(1, m + 1):
        if isSafe(current_vertex, graph, color, c):
            color[current_vertex] = c
            if graphColoringUtil(graph, m, color, current_vertex + 1):
                return True

            # backtrack
            color[current_vertex] = 0


def graphColoring(graph, m):
    color = [0] * V
    if not graphColoringUtil(graph, m, color, 0):
        print("Solution does not exist")
        return False

    printSolution(color)
    return True


# Driver Code
if __name__ == '__main__':
    graph = [[0, 1, 1, 1],
             [1, 0, 1, 0],
             [1, 1, 0, 1],
             [1, 0, 1, 0],
             ]
    m = 3  # Number of colors
    graphColoring(graph, m)
