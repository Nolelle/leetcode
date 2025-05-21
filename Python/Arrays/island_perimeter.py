class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        # best big o time and space is quadratic, constant memory
        perimeter = 0
        # i is rows
        # j is columns

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    perimeter += 4
                    # check cell above
                    if i > 0 and grid[i - 1][j] == 1:
                        perimeter -= 1
                    # check cell below
                    if i < len(grid) - 1 and grid[i + 1][j] == 1:
                        perimeter -= 1
                    # check cell left
                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 1
                    # check cell right
                    if j < len(grid[i]) - 1 and grid[i][j + 1] == 1:
                        perimeter -= 1

        return perimeter
