# https://leetcode.com/problems/non-overlapping-intervals/description/
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        current_end = float("-inf")
        result = 0
        for start, end in sorted(intervals, key=lambda x: x[1]):
            if start < current_end:
                result += 1
            else:
                current_end = end
        return result
