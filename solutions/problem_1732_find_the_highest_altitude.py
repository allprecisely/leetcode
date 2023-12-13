# https://leetcode.com/problems/find-the-highest-altitude/description/

from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = point_altitude = 0
        for point_gain in gain:
            point_altitude += point_gain
            result = max([result, point_altitude])
        return result