class Kruskal:
    def __init__(self, num_nodes):
        self.edges = []
        self.parent = {i: i for i in range(1, num_nodes + 1)}  # Initialize parent dictionary
        self.rank = {i: 0 for i in range(1, num_nodes + 1)}    # Initialize rank dictionary

    def add_edge(self, u, v, w):
        self.edges.append((w, u, v))

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

    def kruskal(self):
        self.edges.sort()  # Sort edges by weight
        minimum_spanning_tree = []

        for edge in self.edges:
            weight, u, v = edge
            if self.find(u) != self.find(v):
                minimum_spanning_tree.append(edge)
                self.union(u, v)

        return minimum_spanning_tree


def main():
    num_nodes = int(input("Enter the number of nodes: "))
    kruskal = Kruskal(num_nodes)
    
    while True:
        print("==========KRUSKAL'S ALGORITHM=================")
        print("\n1. Add Edge\n2. Run Kruskal's Algorithm\n3. Exit\n")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            u, v, w = map(int, input("Enter edge (u, v) and weight separated by space: ").split())
            kruskal.add_edge(u, v, w)
        elif choice == 2:
            min_span_tree = kruskal.kruskal()
            total_cost = sum(edge[0] for edge in min_span_tree)
            print("Minimum Spanning Tree Edges:")
            for edge in min_span_tree:
                print("Edge: ({}, {}) Weight: {}".format(edge[1], edge[2], edge[0]))
            print("Total Cost of Minimum Spanning Tree:", total_cost)
        elif choice == 3:
            break
        else:
            print("Invalid choice! Please enter a valid choice.")


if __name__ == "__main__":
    main()
