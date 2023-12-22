# https://leetcode.com/problems/koko-eating-bananas/description/

from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        temp_h = h
        while left < right:
            middle = (left + right) // 2
            for pile in piles:
                temp_h -= ceil(pile / middle)
            if temp_h < 0:
                left = middle + 1
            else:
                right = middle
            temp_h = h
        return left
            