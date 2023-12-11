# https://leetcode.com/problems/can-place-flowers/description/

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        current_spot = 0
        while len(flowerbed) > current_spot + 1:
            if flowerbed[current_spot]:
                current_spot += 2
            elif flowerbed[current_spot + 1]:
                current_spot += 3
            else:
                current_spot += 2
                n -= 1
                if n == 0:
                    return True
        return n - (len(flowerbed) > current_spot and not flowerbed[current_spot]) == 0
