# https://leetcode.com/problems/unique-paths/description/

from functools import reduce


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return reduce(lambda x, y: x * y, range(n, n + m - 1)) // reduce(lambda x, y: x * y, range(1, m))
