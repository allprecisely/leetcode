# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        current_end = float("-inf")
        result = 0
        for start, end in sorted(points, key=lambda x: x[1]):
            if current_end < start:
                result += 1
                current_end = end
        return result
