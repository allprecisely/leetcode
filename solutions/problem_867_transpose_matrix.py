# https://leetcode.com/problems/transpose-matrix/description/
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [[0] * len(matrix) for _ in range(len(matrix[0]))]
        for i, line in enumerate(matrix):
            for j, element in enumerate(line):
                res[j][i] = element
        return res
