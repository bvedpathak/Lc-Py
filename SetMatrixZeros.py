# Given an m x n integer matrix 'matrix', if an element is 0, 
# set its entire row and column to 0's.
# You must do it in place.

class Solution(object):
    def setZeroes(self, matrix):
        if not matrix:
            return

        m = len(matrix)
        n = len(matrix[0])
        
        # To record the original 0's in 0th row and column
        first_col_zero = False
        first_row_zero = False

        # Check if 0th col has any zeros
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break
        
        # Check if 0th row has any zeros
        for i in range(n):
            if matrix[0][i] == 0:
                first_row_zero = True
                break
        
        # Traverse thru the entire matrix and mark respective first_row and first_col to zero
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        # Now mark the actual rows to zeros
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        
        # Similarly, mark the column to zeros
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        
        # Now set the first row or colmn to zero based on if there was an original zero
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
        
        return matrix

matrix = [[1,1,1],
          [1,0,1],
          [1,1,1]]

matrix = [[0,1,2,0],
          [3,4,5,2],
          [1,3,1,5]]

matrix = [[0,1,2,0],
          [3,4,5,2],
          [1,3,1,5]]

print(f"The resultant matrix is: {Solution().setZeroes(matrix)}")
