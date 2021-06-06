#
# https://leetcode.com/problems/number-of-islands/
#

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

def numIslands(grid):
    def dfs(r, c, rows, cols):
        # always check for bounds first, and then, do value check
        # else, grid[r][c] == '1' will be evaluated first, and will throw
        # array out-of-bound error
        if 0 <= r < rows and 0 <= c < cols and grid[r][c] == '1':
            grid[r][c] = '0'
            dfs(r + 1, c, rows, cols)
            dfs(r - 1, c, rows, cols)
            dfs(r, c + 1, rows, cols)
            dfs(r, c - 1, rows, cols)

    rows, cols = len(grid), len(grid[0])
    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                dfs(r, c, rows, cols)
    return islands

print(numIslands(grid))
