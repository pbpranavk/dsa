
class Graph:
    def __init__(self, size):
        self.adj_matrix = []
        for i in range(size):
            self.adj_matrix.append([0 for i in range(size)])
        self.size = size

    def add_edge(self, v1, v2):
        if v1 == v2:
            print(f"Same vertex {v1} and {v2}")
        else:
            self.adj_matrix[v1][v2] = 1
            self.adj_matrix[v2][v1] = 1

    def remove_edge(self, v1, v2):
        if self.adj_matrix[v1][v2] == 0:
            print(f"No edge between {v1} and {v2}")
        else:
            self.adj_matrix[v1][v2] = 0
            self.adj_matrix[v2][v1] = 0

    def __len__(self):
        return self.size

    def print_matrix(self):
        for row in self.adj_matrix:
            for val in row:
                print(f"{val}", end= " ")
            print("")

g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.print_matrix()