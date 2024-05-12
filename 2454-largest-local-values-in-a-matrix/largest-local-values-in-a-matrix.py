class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        length = len(grid) - 2
        newArr = [[0] * length for _ in range(length)]

        for i in range(length):
            for j in range(length):
                newArr[i][j] = self.getElement(grid, i, j)
        return newArr

    def getElement(self, arr, col, row):
        maximum = 0
        for i in range(3):
            for j in range(3):
                maximum = max(maximum, arr[i + col][j + row])
        return maximum