# https://leetcode.com/problems/domino-and-tromino-tiling/description/

from functools import cache


class Solution:
    with_empty = ((2, False), (1, True))
    without_empty = ((1, False), (1, True), (1, True), (2, False))

    def numTilings(self, n: int) -> int:
        return self.check_variants(n, False) % 1_000_000_007
        
    @cache
    def check_variants(self, n: int, empty: bool) -> int:
        result = 0
        vars = self.with_empty if empty else self.without_empty
        for i, next_empty in vars:
            rem = n - i
            if rem > 1:
                result += self.check_variants(rem, next_empty)
            elif rem == 1:
                result += not next_empty
            elif rem == 0:
                result += not next_empty
        return result
