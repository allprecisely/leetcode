# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/description/

from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row_lenght, column_length = len(grid[0]), len(grid)
        rows, columns = [0] * column_length, [0] * row_lenght
        for i, row in enumerate(grid):
            rows[i] = sum(row) * 2 - row_lenght
            for j, el in enumerate(row):
                if el == 1:
                    columns[j] += 1
                else:
                    columns[j] -= 1
        
        diff = [[0] * row_lenght for _ in range(column_length)]
        for i in range(column_length):
            for j in range(row_lenght):
                diff[i][j] = rows[i] + columns[j]
        return diff
