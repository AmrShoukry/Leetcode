class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        start = 0
        end = rows - 1
        return self.binarySearch(matrix, start, end, columns, target)

    def binarySearch(self, matrix, start, end, columns, target):
        if (start > end):
            return False
        middle = start + (end - start) // 2

        if matrix[middle][0] > target:
            return self.binarySearch(matrix, start, middle - 1, columns, target)
        if matrix[middle][columns - 1] < target:
            return self.binarySearch(matrix, middle + 1, end, columns, target)
        return self.rowBinarySearch(matrix, 0, columns - 1, middle, target)
        
    def rowBinarySearch(self, matrix, start, end, row, target):
        if (start > end):
            return False
        middle = start + (end - start) // 2

        if matrix[row][middle] > target:
            return self.rowBinarySearch(matrix, start, middle - 1, row, target)
        if matrix[row][middle] < target:
            return self.rowBinarySearch(matrix, middle + 1, end, row, target)
        return True