class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        

        ROWS = len(matrix)
        COLS = len(matrix[0])


        rowZero = False
        colZero = False


        for r in range(ROWS):
            if matrix[r][0] == 0:
                colZero = True
                break

        for c in range(COLS):
            if matrix[0][c] == 0:
                rowZero = True
                break



        for r in range(1,ROWS):
            for c in range(1, COLS):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0


        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

        if colZero:
            for r in range(ROWS):
                matrix[r][0] = 0
        return matrix