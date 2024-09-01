class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns = len(matrix[0])
        for y, row in enumerate(matrix):
            for x, number in enumerate(row):
                if number == 0:
                    self.apply_zeroes(matrix, x, y, rows, columns, 555.5)
        for y, row in enumerate(matrix):
            for x, number in enumerate(row):
                if number == 555.5:
                    matrix[y][x] = 0

        
    def apply_zeroes(self, matrix, x, y, rows, columns, number):
        matrix[y][x] = number
        self.apply_zeroes_top(matrix, x, y - 1, number)
        self.apply_zeroes_bottom(matrix, x, y + 1, rows - 1, number)
        self.apply_zeroes_left(matrix, x - 1, y, number)
        self.apply_zeroes_right(matrix, x + 1, y, columns - 1, number)

    def apply_zeroes_top(self, matrix, x, y, number):
        if (y < 0):
            return
        if matrix[y][x] != 0:
            matrix[y][x] = number
        self.apply_zeroes_top(matrix, x, y - 1, number)

    def apply_zeroes_bottom(self, matrix, x, y, max_y, number):
        if (y > max_y):
            return
        if matrix[y][x] != 0:
            matrix[y][x] = number
        self.apply_zeroes_bottom(matrix, x, y + 1, max_y, number)

    def apply_zeroes_left(self, matrix, x, y, number):
        if (x < 0):
            return
        if matrix[y][x] != 0:
            matrix[y][x] = number
        self.apply_zeroes_left(matrix, x - 1, y, number)

    def apply_zeroes_right(self, matrix, x, y, max_x, number):
        if (x > max_x):
            return
        if matrix[y][x] != 0:
            matrix[y][x] = number
        self.apply_zeroes_right(matrix, x + 1, y, max_x, number)



