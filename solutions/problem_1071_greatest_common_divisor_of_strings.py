# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len_str1, len_str2 = len(str1), len(str2)
        while len_str2:
            len_str1, len_str2 = len_str2, len_str1 % len_str2
        result = str1[:len_str1]
        for i, c in enumerate(str1):
            if result[i % len_str1] != c:
                return ""
        for i, c in enumerate(str2):
            if result[i % len_str1] != c:
                return ""
        return result





