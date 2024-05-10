class Tree:
    def __init__(self):
        self.a = [[999] * 20 for _ in range(20)]
        self.visited = [0] * 20
        self.v = 0
        self.e = 0

    def input_data(self):
        self.v = int(input("Enter the number of nodes: "))
        for i in range(self.v):
            self.visited[i] = 0

        self.e = int(input("Enter the number of edges: "))
        for i in range(self.e):
            print("Enter the end nodes of edges:")
            l, u = map(int, input().split())
            w = int(input("Enter the weight/cost of edge: "))
            self.a[l - 1][u - 1] = self.a[u - 1][l - 1] = w

    def display(self):
        print("\nAdjacency matrix:")
        for i in range(self.v):
            print()
            for j in range(self.v):
                print("\t", self.a[i][j], end="")
        print()

    def minimum(self, start_vertex):
        total = 0
        for i in range(self.v):
            self.visited[i] = 0

        self.visited[start_vertex-1] = 1
        for count in range(self.v - 1):
            min_edge = 999
            for i in range(self.v):
                if self.visited[i] == 1:
                    for j in range(self.v):
                        if self.visited[j] != 1:
                            if min_edge > self.a[i][j]:
                                min_edge = self.a[i][j]
                                p = i
                                q = j
            self.visited[q] = 1
            total += min_edge
            print("Minimum cost connection is {} -> {}  with charge: {}".format(p + 1, q + 1, min_edge))

        print("The minimum total cost of connections of all branches is:", total)


def main():
    t = Tree()
    while True:
        print("==========PRIM'S ALGORITHM=================")
        print("\n1. INPUT\n2. DISPLAY\n3. MINIMUM\n4. Exit\n")
        ch = int(input("Enter your choice: "))
        
        if ch == 1:
            print("*******INPUT YOUR VALUES*******")
            t.input_data()
        elif ch == 2:
            print("*******DISPLAY THE CONTENTS********")
            t.display()
        elif ch == 3:
            print("*********MINIMUM************")
            start_vertex = int(input("Enter the start vertex: "))
            t.minimum(start_vertex)
        elif ch == 4:
            break
        else:
            print("Invalid choice! Please enter a valid choice.")


if __name__ == "__main__":
    main()
