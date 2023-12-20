# https://leetcode.com/problems/rotting-oranges/description/

from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = []
        fresh = 0
        for i, row in enumerate(grid):
            for j, orange in enumerate(row):
                if orange == 1:
                    fresh += 1
                elif orange == 2:
                    rotten.append((i, j))
                    fresh += 1
        
        minutes = 0
        while rotten:
            new_rotten = []
            for y, x in rotten:
                fresh -= 1
                if x > 0 and grid[y][x - 1] == 1:
                    grid[y][x - 1] = 2
                    new_rotten.append((y, x - 1))
                if x < len(grid[0]) - 1 and grid[y][x + 1] == 1:
                    grid[y][x + 1] = 2
                    new_rotten.append((y, x + 1))
                if y > 0 and grid[y - 1][x] == 1:
                    grid[y - 1][x] = 2
                    new_rotten.append((y - 1, x))
                if y < len(grid) - 1 and grid[y + 1][x] == 1:
                    grid[y + 1][x] = 2
                    new_rotten.append((y + 1, x))
            minutes += len(new_rotten) != 0
            rotten = new_rotten
        
        return minutes if fresh == 0 else -1
                
                
