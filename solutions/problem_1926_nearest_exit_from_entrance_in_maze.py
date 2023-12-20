# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/description/

from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = [(entrance[1], entrance[0])]
        maze[entrance[0]][entrance[1]] = '+'
        result = 0
        while queue:
            adjoin = []
            for x, y in queue:
                if x > 0:
                    if maze[y][x - 1] == '.':
                        adjoin.append((x - 1, y))
                        maze[y][x - 1] = '+'
                elif result: return result
                if x < len(maze[0]) - 1:
                    if maze[y][x + 1] == '.':
                        adjoin.append((x + 1, y))
                        maze[y][x + 1] = '+'
                elif result: return result
                if y > 0:
                    if maze[y - 1][x] == '.':
                        adjoin.append((x, y - 1))
                        maze[y - 1][x] = '+'
                elif result: return result
                if y < len(maze) - 1:
                    if maze[y + 1][x] == '.':
                        adjoin.append((x, y + 1))
                        maze[y + 1][x] = '+'
                elif result: return result
            queue = adjoin
            result += 1
        return -1
