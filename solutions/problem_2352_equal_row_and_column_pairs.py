# https://leetcode.com/problems/equal-row-and-column-pairs/description/

from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        result = 0

        rows_sets = tuple(set(row) for row in grid)
        columns = tuple([] for _ in range(len(grid)))
        columns_sets = tuple(set() for _ in range(len(grid)))
        for row in grid:
            for j, el in enumerate(row):
                columns_sets[j].add(el)
                columns[j].append(el)
        
        for i, row in enumerate(rows_sets):
            for j, column in enumerate(columns_sets):
                if row == column and grid[i] == columns[j]:
                    result += 1
        
        return result
        