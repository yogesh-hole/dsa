# Find all possible paths between two vertices

class Graph:
    def __init__(self, v):
        self.V = v
        self.adj = [[] for i in range(self.V)]

    def addEdge(self, u, v):
        self.adj[u].append(v)

    # Returns the count of paths from source and destination
    def count_paths(self, source, destination):
        # Mark all vertices as not visited
        visited = [False] * self.V

        # Call the recursive helper function to print all paths
        path_count = [0]
        self.count_path_utils(source, destination, visited, path_count)
        return path_count[0]

    # A recursive function to print all paths from source to destination.
    # visited keeps track of vertices in current path. path[] stores actual vertices.
    # path_index is current index in path

    def count_path_utils(self, u, destination, visited, path_count):
        visited[u] = True

        # if current vertex is same as destination then increment count
        if u == destination:
            path_count[0] += 1

        # recur all the vertices adjacent to current vertx
        i = 0
        while i < len(self.adj[u]):
            if not visited[self.adj[u][i]]:
                self.count_path_utils(self.adj[u][i], destination, visited, path_count)
            i += 1

        visited[u] = False

# Driver Code
if __name__ == '__main__':

    # Create a graph given in the
    # above diagram
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(2, 0)
    g.addEdge(2, 1)
    g.addEdge(1, 3)

    s = 2
    d = 3

    # Function call
    print(g.count_paths(s, d))