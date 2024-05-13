import math

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        score = 0
        change = False
        counter = 0

        for i in range(m):
            change = False
            if grid[i][0] == 0:
                change = True
            for j in range(n):
                if change:
                    grid[i][j] = abs(grid[i][j] - 1)

        for j in range(n):
            counter = 0
            change = False
            for i in range(m):
                if grid[i][j] == 0:
                    counter += 1
            if counter >= math.ceil(m / 2):
                change = True
            for i in range(m):
                if change:
                    grid[i][j] = abs(grid[i][j] - 1)
                score += grid[i][j] * math.pow(2, (n - j - 1))

        return int(score)
        

