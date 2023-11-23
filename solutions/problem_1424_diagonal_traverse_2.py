# https://leetcode.com/problems/diagonal-traverse-ii/description/
from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        result = []
        for i in range(len(nums)):
            for j, num in enumerate(nums[i]):
                line = i + j
                if len(result) <= line:
                    result.append([num])
                else:
                    result[line].append(num)
        return [num for line in result for num in reversed(line)]
