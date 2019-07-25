class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        perimeter = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # if grid value is 1 we check values up, down, left, and right of it
                if grid[i][j] == 1:
                    # if tile is on the top edge, add 1 to perimeter
                    if i == 0:
                        perimeter = perimeter  + 1
                    # if tile is on the left edge, add 1 to permiter
                    if j == 0:
                        perimeter = perimeter  + 1
                    # if tile is on the bottom edge, add 1 to perimeter
                    if i == len(grid)-1:
                        perimeter = perimeter  + 1
                    # if tile is on the right edge, add 1 to perimeter
                    if j == len(grid[0])-1:
                        perimeter = perimeter  + 1
                    # check top for 0
                    if i > 0 and grid[i-1][j] == 0:
                        perimeter = perimeter + 1
                    # check left for 0
                    if j > 0 and grid[i][j-1] == 0:
                        perimeter = perimeter + 1
                    # check bottom for 0
                    if i < len(grid)-1 and grid[i+1][j] == 0:
                        perimeter = perimeter + 1
                    # check right for 0
                    if j < len(grid[0])-1 and grid[i][j+1] == 0:
                        perimeter = perimeter + 1

        return perimeter
