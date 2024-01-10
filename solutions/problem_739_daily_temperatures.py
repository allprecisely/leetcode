# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                ind = stack.pop()
                result[ind] = i - ind
            stack.append(i)
        return result
