# https://leetcode.com/problems/longest-common-subsequence/description/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) > len(text2):
            return self.longestCommonSubsequence(text2, text1)
        matrix = [0] * (len(text2) + 1)
        for c1 in text1:
            prev = 0
            for i, c2 in enumerate(text2):
                prev, matrix[i + 1] = matrix[i + 1], prev + 1 if c1 == c2 else max(matrix[i + 1], matrix[i])
        return matrix[-1]
