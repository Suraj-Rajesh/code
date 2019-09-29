class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        
        # there will be floor(n/2) squares that we would need to deal with
        for x in range(n//2):
            
            # take each group of 4 elements to rotate
            for y in range(x, n - 1 - x):
                tmp                         = matrix[x][y]
                matrix[x][y]                = matrix[n -1 - y][x]
                matrix[n - 1 - y][x]        = matrix[n - 1 -x][n - 1 - y]
                matrix[n - 1 - x][n - 1 -y] = matrix[y][n - 1 - x]
                matrix[y][n - 1 - x]        = tmp
                
            #
            # INPUT MATRIX
            #
            #  1   2   3   4
            #  5   6   7   8
            #  9  10  11  12
            # 13  14  15  16
            #
            # CLOCKWISE ROTATED OUTPUT MATRIX
            #
            #  13   9   5   1
            #  14  10   6   2 
            #  15  11   7   3 
            #  16  12   8   4
            #
            # OBSERVATION:
            # 
            # You can see, entire rows gets shifted as a column. Observe, 1, 2, 3, 4 in input and output matrix.
            #
            # As you can see, there are two squares in the input matrix.
            #
            # SQUARE 1:
            #
            #  1   2   3   4 
            #  5           8 
            #  9          12
            # 13  14  15  16
            #
            #
            #  SQUARE 2:
            #
            #     6   7 
            #    10  11
            #
            # Hence, outer loop is n//2.
            #
            #
            # Next, we move elements in groups of 4.
            #
            #  1, 4, 16, 13 rotate
            #  2, 8,  9, 15 rotate
            #  3, 12, 14, 5 rotate
            #
            # In one square, these movements happen x -> (n - 2 - x) times, hence the second loop, for y in range(x, n - 1 -x): (remember in range, last element is not included).
            # For example, if you take x = 0, then above, we need three iterations, which is 0 -> (4 - 2 - 0) = 0 -> 2.
            #
            # To arrive at co-ordinates, take the second set of elements in a 4 * 4 matrix.
            # In our case, it would be 2, 8, 9, 15
            #
            # Start with first element 2, (x, y) = (0, 1) = 2
            # Now, we have, x = 0, y = 1, use that to derive the rest,
            # 8 = (1, 3), which in terms of x and y is, (y, n - 1 -x) [NOTE: we do -x to (n - 1), since we loop and the square becomes smaller]
            # 15 = (3, 2) = (n - 1 - x, n - 1 - y)
            # 9 = (2, 0) = (n - 1 - y, x)
            #
            # Once we have them, all we need is to swap, by having just one temp variable.
            #
