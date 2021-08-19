import copy


class FindAnimals:
    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)
        self.grid_count = copy.deepcopy(grid)
        self.maxSize = 0

    def findAnimals(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == 1:
                    # row, col = 0, 0
                    self.grid_count[row][col] = -1
                    maxSize = self.dfs(row, col)
                    self.updateCount(maxSize)
                    if maxSize > self.maxSize:
                        self.maxSize = maxSize

        return self.grid_count, self.maxSize

    def isValidMove(self, row, col):
        if 0 <= row < len(self.grid) and 0 < col < len(self.grid[row]) and \
                self.grid[row][col] == 1:
            return True
        else:
            return False

    def dfs(self, row, col):
        print("Exploring node {}".format((row, col)))
        # Mark as visited
        self.grid[row][col] = 0

        rowActions = [-1, -1, -1, 0, 1, 1, 1, 0]
        colActions = [-1, 0, 1, 1, 1, 0, -1, -1]
        maxCount = 1

        for r, c in zip(rowActions, colActions):
            next_row = row + r
            next_col = col + c

            print('You are moving to {} {}'.format(next_row, next_col))
            if self.isValidMove(next_row, next_col):
                self.grid_count[next_row][next_col] = -1
                maxCount += self.dfs(next_row, next_col)

        return maxCount

    def updateCount(self, maxSize):
        for row in range(len(self.grid_count)):
            for col in range(len(self.grid_count[row])):
                if self.grid_count[row][col] == -1:
                    self.grid_count[row][col] = maxSize


grid1 = [
    [1, 1, 0, 1],
    [0, 1, 0, 1],
    [0, 0, 0, 0],
    [1, 0, 0, 0]
]
fa = FindAnimals(grid1)
output, maxSize = fa.findAnimals()

for row in grid1:
    print(row)
print("****************")
for row in output:
    print(row)
print("Maximum size is {}".format(maxSize))
