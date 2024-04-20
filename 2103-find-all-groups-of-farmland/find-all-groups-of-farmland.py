class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m = len(land)
        n = len(land[0])
        solutions = []

        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    max_row = [i]
                    max_col = [j]
                    self.get_values(i, j, land, m, n, max_row, max_col)
                    solutions.append([i, j, max_row[0], max_col[0]])

        return solutions

    def get_values(self, i, j, land, max_i, max_j, max_row, max_col):
        if (land[i][j] == 0):
            return
        land[i][j] = 0

        if i > max_row[0]:
            max_row[0] = i
        if j > max_col[0]:
            max_col[0] = j

        if (i - 1 >= 0):
            self.get_values(i - 1, j, land, max_i, max_j, max_row, max_col)
        if (i + 1 < max_i):
            self.get_values(i + 1, j, land, max_i, max_j, max_row, max_col)
        if (j - 1 >= 0):
            self.get_values(i, j - 1, land, max_i, max_j, max_row, max_col)
        if (j + 1 < max_j):
            self.get_values(i, j + 1, land, max_i, max_j, max_row, max_col)


