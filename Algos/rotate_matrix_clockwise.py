#
# this solution takes extra space for out matrix. Look at Solution() for in-place
#
def rotate_anti_clockwise_extra_space(matrix):
    n = len(matrix)
    rows = cols = n
    out_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for r in range(n):
        for c in range(n):
            out_matrix[n - 1 - c][r] = matrix[r][c]
    return out_matrix

class Solution:
    def rotate_clockwise(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        
        # there will be floor(n/2) squares that we would need to deal with
        for r in range(n//2):
            
            # take each group of 4 elements to rotate (give special attention here, if n = 4, x = 0, then we iterate only 3 times)
            # note that n below always accompanied by -1, so we see n - 1 everywhere n is used
            for c in range(r, n - 1 - r):
                tmp                          = matrix[r][c]
                matrix[r][c]                 = matrix[n -1 - c][r]
                matrix[n - 1 - c][r]         = matrix[n - 1 -r][n - 1 - c]
                matrix[n - 1 - r][n - 1 - c] = matrix[c][n - 1 - r]
                matrix[c][n - 1 - r]         = tmp
                
    def rotate_anti_clockwise(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        
        # there will be floor(n/2) squares that we would need to deal with
        for r in range(n//2):
            
            # take each group of 4 elements to rotate (give special attention here, if n = 4, x = 0, then we iterate only 3 times)
            for c in range(r, n - 1 - r):
                tmp                      = matrix[r][c]
                matrix[r][c]             = matrix[c][n -1 -r]
                matrix[c][n -1 -r]       = matrix[n -1 -r][n -1 -c]
                matrix[n -1 -r][n -1 -c] = matrix[n -1 - c][r]
                matrix[n -1 -c][r]       = tmp
                
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
            # In one square, these movements happen r -> (n - 2 - r) times, hence the second loop, for c in range(r, n - 1 - c): (remember in range, last element is not included).
            # For example, if you take x = 0, then above, we need three iterations, which is 0 -> (4 - 2 - 0) = 0 -> 2.
            #
            # To arrive at co-ordinates, take the second set of elements in a 4 * 4 matrix.
            # In our case, it would be 2, 8, 9, 15
            #
            # Start with first element 2, (r, c) = (0, 1) = 2
            # Now, we have, r = 0, c = 1, use that to derive the rest,
            # 8 = (1, 3), which in terms of r and c is, (c, n - 1 - r) [NOTE: we do -r to (n - 1), since we loop and the square becomes smaller]
            # 15 = (3, 2) = (n - 1 - r, n - 1 - c)
            # 9 = (2, 0) = (n - 1 - c, r)
            #
            # Once we have them, all we need is to swap, by having just one temp variable.
            #
