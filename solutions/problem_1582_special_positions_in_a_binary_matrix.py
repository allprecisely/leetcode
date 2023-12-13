# https://leetcode.com/problems/special-positions-in-a-binary-matrix/description/

from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        result = 0
        ones_in_rows, ones_in_columns = [0] * len(mat), [0] * len(mat[0])
        for i, row in enumerate(mat):
            for j, val in enumerate(row):
                if val == 1:
                    ones_in_rows[i] += 1
                    ones_in_columns[j] += 1

        for i, row in enumerate(mat):
            for j, val in enumerate(row):
                if val == 1 and ones_in_rows[i] == 1 and ones_in_columns[j] == 1:
                    result += 1

        return result
