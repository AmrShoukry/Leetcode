class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands = 0

        for i in range(m):
            for j in range(n):
                if (grid[i][j] == "1"):
                    islands += 1
                    self.flip(m, n, grid, i, j)
        return islands


    def flip(self, m, n, grid, i, j):
        if (grid[i][j] == "0"):
            return
        grid[i][j] = "0"
        if (i - 1 >= 0):
            self.flip(m, n, grid, i - 1, j)
        if (i + 1 < m):
            self.flip(m, n, grid, i + 1, j)
        if (j - 1 >= 0):
            self.flip(m, n, grid, i, j - 1)
        if (j + 1 < n):
            self.flip(m, n, grid, i, j + 1)
