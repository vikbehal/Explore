class connectedGraph:
    def __init__(self, graph):
        self.graph = graph

    def explore(self, row, col):
        if row < 0 or col < 0 or row >= len(self.graph) or col >= len(self.graph[row]):
            return 0
        if self.graph[row][col] == 0:
            return 0

        self.graph[row][col] = 0
        size = 1
        print("row {} col {}".format(row, col))
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                print("exploring {}".format((r, c)))
                if r != row or c != col:
                    size += self.explore(r, c)
        return size

    def traverse(self):
        maxSize = 0
        for row, rowVal in enumerate(self.graph):
            for col, colVal in enumerate(self.graph[row]):
                if colVal == 1:
                    size = self.explore(row, col)
                    maxSize = max(size, maxSize)

        return maxSize


graph = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]]
cg = connectedGraph(graph)
print("*************\nMaximum connected cells are {}".format(cg.traverse()))
