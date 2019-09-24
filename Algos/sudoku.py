def get_empty_slot(arr):
    for row in range(9):
        for col in range(9):
            if arr[row][col] == 0:
                return (row, col)

    return (-1, -1)


def row_satisfied(arr, row, num):
    for col in range(9):
        if num == arr[row][col]:
            return False

    return True

def col_satisfied(arr, col, num):
    for row in range(9):
        if num == arr[row][col]:
            return False

    return True

def grid_satisfied(arr, row, col, num):
    (baser, basec) = (row - row % 3, col - col % 3)
    for i in range(baser, baser + 3):
        for j in range(basec, basec + 3):
            if arr[i][j] == num:
                return False

    return True

def cond_satisfied(arr, row, col, num):
    return row_satisfied(arr, row, num) and col_satisfied(arr, col, num) and grid_satisfied(arr, row, col, num)


def sudoku_solver(arr):
    row, col = get_empty_slot(arr)

    if row == -1:
        return True

    for num in range(1, 10):
        if cond_satisfied(arr, row, col, num):
            arr[row][col] = num

            if sudoku_solver(arr):
                return True

            arr[row][col] = 0

    return False

def print_grid(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j]),
        print('\n')

grid=[[3,0,6,5,0,8,4,0,0],
      [5,2,0,0,0,0,0,0,0],
      [0,8,7,0,0,0,0,3,1],
      [0,0,3,0,1,0,0,8,0],
      [9,0,0,8,6,3,0,0,5],
      [0,5,0,0,9,0,6,0,0],
      [1,3,0,0,0,0,2,5,0],
      [0,0,0,0,0,0,0,7,4],
      [0,0,5,2,0,6,3,0,0]]

sudoku_solver(grid)
print_grid(grid)
